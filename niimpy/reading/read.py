"""Read data from various formats, user entery point.

This module contains various functions `read_*` which load data from different
formats into pandas.DataFrame:s.  As a side effect, it provides the
authoritative information on how incoming data is converted to dataframes.

"""

import pandas as pd
import warnings
import json

from niimpy.reading import database
from niimpy.preprocessing import util

def _read_preprocess(df, add_group=None):
    """Standard preprocessing arguments when reading.

    This is a preprocessing filter which handles some standard arguments
    when reading files.  This should be considered a private, unstable
    function.


    Parameters
    ----------

    df: pandas.DataFrame

        Input data frame

    add_group: string, optional

        If given, add a new 'group' column with all values set to this
        given identifier.


    Returns
    -------

    df: dataframe

        Resulting dataframe (modified in-place if possible, but may also
        be a copy)

    """
    if add_group is not None:
        df['group'] = add_group
        #df['group'] = df['group'].astype('category')
        #pd.Categorical(add_group)
    return df


def read_sqlite(filename, table, add_group=None, user=database.ALL, limit=None, offset=None, start=None, end=None, tz=None):
    """Read DataFrame from sqlite3 database

    This will read data from a sqlite3 file, taking sensor data in a
    given table, and optionally apply various limits.

    Parameters
    ----------

    filename : str
        filename of sqlite3 database

    table : str
        table name of data within the database

    add_group : object
        If given, add a 'group' column with all values set to this.

    user : str or database.ALL, optional
        If given, return only data matching this user (based an column 'user')

    limit : int, optional
        If given, return only this many rows

    offset : int, optional
        When used with limit, skip this many lines at the beginning

    start : int or float or str or datetime.datetime, optional
        If given, limit to this starting time.  Formats can be int/float
        (unixtime), string (parsed with dateutil.parser.parser, or
        datetime.datetime.

    end : int or float or str or datetime.datetime, optional
        Same meaning as 'start', but for end time
    """
    if tz is None:
        warnings.warn(DeprecationWarning("From now on, you should explicitely specify timezone with e.g. tz='Europe/Helsinki'"), stacklevel=2)

    db = database.Data1(filename, tz=tz)
    df = db.raw(table, user, limit=limit, offset=offset, start=start, end=end)
    df = _read_preprocess(df, add_group=add_group)
    return df


def read_sqlite_tables(filename):
    """Return names of all tables in this database

    Return a set of all tables contained in this database.  This may be
    useful when you need to see what data is available within a database.
    """
    db = database.Data1(filename)
    return db.tables()

def _get_dataframe(df_or_database, table, user=None):
    """Read from database or directly use DataFrame

    Functions used to accept a database only, now the standard is
    dataframe.  This provides some backwards compatability between the
    old and new systems: DataFrames are used as-is, but if a database is
    given, it extracts the right information out of the table (and does
    what the database used to do to filter by user).  This function
    could also be used to transparently accept other types of data
    inputs.

    If input is:

    - atabase: extract the given table/user using .raw() and return

    A typical usage is::

        def function(df):
            # 'df' could be a DataFrame or database
            df = _get_dataframe(df, 'TableName')
            # 'df' is now always a DataFrame

    Returns
    -------
    df : DataFrame (same one if possible)

    """
    if isinstance(df_or_database, database.Data1):
        df = df_or_database.raw(table=table, user=subject)
    else:
        df = df_or_database
        # questions was *not*  dataframe.
        if user is not None and user is not database.ALL:
            df = df[df['user'] == user]
    return df





def read_csv(filename, read_csv_options={}, add_group=None,
             tz=None):
    """Read DataFrame from csv file

    This will read data from a csv file and then process the result with
    `niimpy.util.df_normalize`.


    Parameters
    ----------

    filename : str
        filename of csv file

    read_csv_options: dict
        Dictionary of options to pandas.read_csv, if this is necessary for custom
        csv files.

    add_group : object
        If given, add a 'group' column with all values set to this.

    """
    if tz is None:
        warnings.warn(DeprecationWarning("From now on, you should explicitely specify timezone with e.g. tz='Europe/Helsinki'"), stacklevel=2)

    df = pd.read_csv(filename, **read_csv_options)

    # df_normalize converts sets the index to time values and does other time
    # conversions.  Inplace.
    util.df_normalize(df, tz=tz)
    df = _read_preprocess(df, add_group=add_group)
    return df

def read_csv_string(string, tz=None):
    """Parse a string containing CSV and return dataframe

    This should not be used for serious reading of CSV from disk, but
    can be useful for tests and examples.  Various CSV reading options
    are turned on in order to be better for examples:

    - Allow comments in the CSV file

    - Remove the `datetime` column (redundant with `index` but some
      older functions break without it, so default readers need to leave
      it).

    Parameters
    ----------
    string : string containing CSV file


    Returns
    -------
    df: pandas.DataFrame
    """
    if tz is None:
        warnings.warn(DeprecationWarning("From now on, you should explicitely specify timezone with e.g. tz='Europe/Helsinki'"), stacklevel=2)
    import io
    df = read_csv(io.StringIO(string),
                  tz=tz,
                  read_csv_options={
                      'comment': '#',
                      },
                 )
    if 'datetime' in df.columns:
        del df['datetime']
    return df




def format_mhealth_time_interval(df, prefix):
    ''' Format a database containing columns in the mHealth time interval.
    
    A time interval in the mHealth format has either
     - a date and a time of day (morning, afternoon, evening or night), or
     - two of start time, end time and duration.

    In the first case, the formatted database will contain two columns:
    measure_date and time_of_day.

    In the second case, the formatted database will contain two columns:
    start_time and duration (as a timedelta64).
    '''
    df["start_time"] = None
    df["duration"] = None

    start_col = f'{prefix}.start_date_time'
    end_col = f'{prefix}.end_date_time'
    duration_value_col = f'{prefix}.duration.value'
    duration_unit_col = f'{prefix}.duration.value'
    
    if start_col in df.columns:
        rows = ~df[start_col].isnull()
        df.loc[rows, "start_time"] = pd.to_datetime(df.loc[rows, start_col])

    if end_col in df.columns:
        rows = ~df[end_col].isnull()
        df.loc[rows, end_col] = pd.to_datetime(df.loc[rows, end_col])

    if duration_value_col in df.columns:
        rows = ~df[duration_value_col].isnull()
        value = df.loc[rows, duration_value_col]
        unit = df.loc[rows, duration_unit_col]
        df.loc[rows, "duration"] = pd.to_timedelta(value, unit=unit)

    if start_col in df.columns and end_col in df.columns:
        rows = ~df[end_col].isnull() & ~df[start_col].isnull()
        df.loc[rows, "duration"] = pd.to_datetime(df.loc[rows, end_col]) - pd.to_datetime(df.loc[rows, "start_time"])

    return df



def read_mhealth_total_sleep_time(data_list):
    df = pd.json_normalize(data_list)
    total_sleep_time_columns = {
        "total_sleep_time.value": "total_sleep_time",
        "total_sleep_time.unit": "total_sleep_time_unit",
        "effective_time_frame.time_interval.start_date_time": "effective_start_time",
        "effective_time_frame.time_interval.end_date_time": "effective_end_time",
    }
    total_sleep_time_time_columns = ["effective_start_time", "effective_end_time"]

    df = format_mhealth_time_interval(df, "effective_time_frame.time_interval")

    df = df.rename(columns=total_sleep_time_columns)
    for col in total_sleep_time_time_columns:
        df[col] = pd.to_datetime(df[col])

    df["timestamp"] = df["effective_start_time"]
    df.set_index('timestamp', inplace=True)
    return df


def read_mhealth_total_sleep_time_from_file(filename):
    with open(filename) as f:
        data = json.load(f)

    df = read_mhealth_total_sleep_time(data)

    return df
