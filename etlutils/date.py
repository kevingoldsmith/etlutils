"""etlutils.date consists of functions useful for manipulating or converting
dates between different formats
"""

import datetime
import time
import dateutil.tz


def mkdate(datestr):
    """Creates a date object for a string in the format YYYY-MM-DD

    useful for parsing a data from the command line or from a filename or in a
    file

    Args:
        datestr: a string in the format "YYYY-MM-DD"

    Returns:
        a datetime.date object

    Raises:
        ValueError: if the string is in the wrong format
    """
    try:
        fulltime = time.strptime(datestr, '%Y-%m-%d')
        return datetime.date(fulltime.tm_year, fulltime.tm_mon,
                             fulltime.tm_mday)
    except ValueError:
        raise ValueError(f'{datestr} is not a proper date string')


def get_date_from_timestamp(timestamp, offset=0):
    """creates a datetime.datetime object from a timestamp with offset

    Using a twitter-style timestamp and offset return a datetime object

    Args:
        timestamp: a unix-type timestamp
        offset: a timezone offset in minutes from GMT

    Returns:
        a datetime.datetime object
    """
    return datetime.datetime.fromtimestamp(timestamp,
                                           tz=dateutil.tz.tzoffset(None,
                                                                   offset*60))


def datetime_from_zulutime_string(utc_time_string):
    """Given a utc_time_string, create a datetime.datetime object

    creates a datetime object from a utc-formatted time string

    Args:
        utc_time_string: utc formatting string

    Returns:
        a datetime.datetime object
    """

    try:
        return datetime.datetime.strptime(utc_time_string,
                                          '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        # this sometimes happens if the fractional value
        # is left off the seconds
        return datetime.datetime.strptime(utc_time_string,
                                          '%Y-%m-%dT%H:%M:%SZ')
