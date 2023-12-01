import pandas as pd
import numpy as np

import niimpy
from niimpy import config


def test_read_mhealth_total_sleep_time():
    """test reading mixed mhealth data from the example file."""
    data = niimpy.reading.mhealth.total_sleep_time_from_file(config.MHEALTH_TOTAL_SLEEP_TIME_PATH)
    assert data['total_sleep_time'][0] == pd.Timedelta(465, unit="minutes")
    assert data['descriptive_statistic'][1] == "average"
    assert data['descriptive_statistic_denominator'][1] == "d"
    assert data['date'][3] == pd.to_datetime("2013-02-05")
    assert data['part_of_day'][3] == "evening"
    assert data['start'][0] == pd.to_datetime("2016-02-06 04:35:00+00:00")
    assert data['end'][0] == pd.to_datetime("2016-02-06 14:35:00+00:00")
    assert data['start'][2] == pd.to_datetime("2013-01-26 07:35:00+00:00")
    assert data['end'][2] == pd.to_datetime("2013-02-05 07:35:00+00:00")

def test_read_mhealth_heart_rate():
    """test reading mixed mhealth data from the example file."""
    data = niimpy.reading.mhealth.heart_rate_from_file(config.MHEALTH_HEART_RATE_PATH)
    assert data['heart_rate'][0] == 70
    assert data['heart_rate'][1] == 65
    assert data['descriptive_statistic'][2] == "average"
    assert data['temporal_relationship_to_sleep'][2] == "during sleep"
    assert data['temporal_relationship_to_sleep'][0] == "on waking"
    assert data['start'][2] == pd.to_datetime("2023-12-20T01:50:00-02:00")

