from eautils.date import *
import pytest
import datetime
import time


def test_mkdate():
    assert mkdate('2019-04-02') == datetime.date(2019,4,2)
    with pytest.raises(ValueError):
        mkdate('2019-')


def test_get_date_from_timestamp():
    now_as_timestamp = time.time()
    assert get_date_from_timestamp(now_as_timestamp) == datetime.datetime.fromtimestamp(now_as_timestamp, tz=dateutil.tz.tzoffset(None,0))
    timestamp = 1590299356.217945
    assert get_date_from_timestamp(timestamp) == datetime.datetime(2020, 5, 24, 5, 49, 16, 217945, tzinfo=dateutil.tz.tzoffset(None, 0))
    assert get_date_from_timestamp(timestamp, 6) == datetime.datetime(2020, 5, 24, 5, 55, 16, 217945, tzinfo=dateutil.tz.tzoffset(None, 360))


def test_datetime_from_string():
    assert datetime_from_string("2011-08-12T20:17:46.384Z") == datetime.datetime(2011, 8, 12, 20, 17, 46, 384000)

