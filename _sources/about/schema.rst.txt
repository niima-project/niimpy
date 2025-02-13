Data schema
===========

This page documents the expected data schema of Niimpy.  This is a
general description that applies to all different types of data that
Niimpy can handle, and mainly describes measurement metadata.
Specific types of data (e.g. location data) will have additional
columns containing the actual data.

By using a standardized schema (mainly column names), we can promote
interoperability of various tools.



Format
------

Data is in a tabular (relational) format.  A row is an observation,
and columns are properties of observations.  (At this level of
abstraction, an "observation" may be one measurement, or processed
combination of multiple measurements).

In Niimpy, this is internally stored and handled as a
pandas.DataFrame.  The schema naturally maps to the columns/rows of
the DataFrames.

The on-disk format is currently irrelevant, as long as the producers
can create a DataFrame of the necessary format.  Currently, we provide
support sqlite3 and csv.

Additionally, we provide readers for MHealth data and Google Takeout
data. These readers convert the data to the standard DataFrame format.



Standard columns in DataFrames
------------------------------

By having standard columns, we can create portable functions that
easily operate on diverse data types.

* The **DataFrame index** should be a ``pandas.DatetimeIndex``.

  The index should represent the time the measurement was taken.
  If the measurement represents a period of time, the index should
  be the starting time of the period.

* ``user``: opaque identifier for the user.  Often a string or
  integer.

* ``device``: unique identifier for a user's device (not the
  device type).  For example, a user could have multiple phones, and
  each would have a separate ``device`` identifier.

* ``time``: This is optional at runtime but is used in on disk formats.
  
  The timestamp of the observation, in unixtime (seconds
  since 00:00 on 1970-01-01), stored as an integer.  Unixtime is a
  globally unique measure
  of an instance of time on Earth, and to get localtime it is combined
  with a timezone.

  In on-disk formats, ``time`` is considered the master timestamp,
  many other time-based properties are computed from it (though you
  could produce your own DataFrames other ways).  In some of the
  standard formats (CSV/sqlite3), when a file is read, this integer
  column is automatically converted to the ``datetime`` column below
  and the DataFrame index.



Exploration, analysis and exploration modules expect specific input data columns, representing the actual data.
For example, the location module expects latitude and longitude columns.
These columns are documented in the User Guide sections for each module.




Standard columns in on-disk formats
-----------------------------------

For the most part, this maps directly to the columns you see above.
An on-disk format should have a ``time`` column (unixtime, integer)
and data columns as described above.



