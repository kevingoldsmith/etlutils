import datetime
import time
import dateutil.tz


def mkdate(datestr):
    try:
        fulltime = time.strptime(datestr, '%Y-%m-%d')
        return datetime.date(fulltime.tm_year, fulltime.tm_mon, fulltime.tm_mday)
    except ValueError:
        raise ValueError(f'{datestr} is not a proper date string')


def get_date_from_timestamp(timestamp, offset):
    return datetime.datetime.fromtimestamp(timestamp, tz=dateutil.tz.tzoffset(None, offset*60))


def datetime_from_string(utc_time_String):
    return datetime.datetime.strptime(utc_time_String, '%Y-%m-%dT%H:%M:%S.%fZ')
