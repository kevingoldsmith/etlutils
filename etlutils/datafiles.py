"""etlutils.datafiles contains methods useful for producing and consuming data
for structured data
"""

import os
import time
import dateutil
import datetime
import json
import dateutil.relativedelta


def __dump_json_file(file_path, data, indent=True):
    with open(file_path, "w") as f:
        if indent:
            f.write(json.dumps(data, indent=2))
        else:
            f.write(json.dumps(data))
    time.sleep(1)


def get_yearly_file_path(directory, datatype, year, file_extension='json',
                         make_directories=True):
    """puts together a path to a file for data that is saved by year

    will create the directory if needed and set up the filename in a consistent
    way. doesn't do any error checking, so empty strings are not illegal, but
    will produce crummy filenames

    the format is of the structure
    <directory>/<datatype>_<year>.<file_extension>

    Args:
        directory: the directory under which the file will be created
        datatype: the root of the filename
        year: the integer year to append, will expanded to four digits if
              fewer, does not validate
        file_extension: the extention (without the .)
        make_directories: will create directory if it does not exist when True

    Returns:
        A string path composed of the arguments
    """
    if directory and make_directories and (not os.path.exists(directory)):
        os.mkdir(directory)
    rootname = ''
    if datatype:
        rootname = datatype + '_'
    return os.path.join(directory, f'{rootname}{year:04}.{file_extension}')


def get_monthly_file_path(directory, datatype, year, month,
                          file_extension='json', make_directories=True):
    """puts together a path to a file for data that is saved by month

    will create the directory if needed and set up the filename in a consistent
    way. doesn't do any error checking, so empty strings are not illegal, but
    will produce crummy filenames

    the format is of the path is
    <directory>/<year>/<datatype>_<year>-<month>.<file_extension>

    Args:
        directory: the directory under which the file will be created
        datatype: the root of the filename
        year: the integer year to append, will expanded to four digits if
              fewer, does not validate
        month: the integer month to append, will expanded to two digits if
               fewer, does not validate
        file_extension: the extention (without the .)
        make_directories: will create directory if it does not exist when True

    Returns:
        A string path composed of the arguments
    """
    path = os.path.join(directory, f'{year:04}')
    if make_directories:
        os.makedirs(path, exist_ok=True)
    rootname = ''
    if datatype:
        rootname = datatype + '_'
    return os.path.join(path,
                        f'{rootname}{year:04}-{month:02}.{file_extension}')


def get_daily_file_path(directory, datatype, year, month, day,
                        file_extension='json', make_directories=True):
    """puts together a path to a file for data that is saved by day

    will create the directories if needed and set up the filename in a
    consistent way. doesn't do any error checking, so empty strings are not
    illegal, but will produce crummy filenames

    the format is of the structure
    <directory>/<year>/<year>-<month>-<day>/<datatype>.<file_extension>

    Args:
        directory: the directory under which the file will be created
        datatype: the root of the filename
        year: the integer year to append, will expand to four digits if fewer,
              does not validate
        month: the integer month to append, will expand to two digits if fewer,
               does not validate
        day: the integer day to append, will expand to two digits if fewer,
             does not validate
        file_extension: the extention (without the .)
        make_directories: will create directory if it does not exist when True

    Returns:
        A string path composed of the arguments
    """
    path = os.path.join(directory, f'{year:04}',
                        f'{year:04}-{month:02}-{day:02}')
    if make_directories:
        os.makedirs(path, exist_ok=True)
    return os.path.join(path, f'{datatype}.{file_extension}')


def dump_to_yearly_json_file(directory, year, data, datatype=''):
    """saves data to a yearly file stored in JSON

    will create the directories if needed and set up the filename in a
    consistent way, doesn't do any error checking, so empty strings are not
    illegal, but will product crummy filenames

    the format of the path is
    <directory>/<datatype>_<year>.json

    Args:
        directory: the directory under which the file will be created
        year: the integer year to append, will expand to four digits if fewer,
              does not validate
        data: a JSON serializable data structure
        datatype: the root of the filename

    Returns:
        The path to the file that was created
    """
    filename = get_yearly_file_path(directory, datatype, year)
    __dump_json_file(filename, data)
    return filename


def dump_to_monthly_json_file(directory, year, month, data, datatype=''):
    """saves data to a monthly file stored in JSON

    will create the directories if needed and set up the filename in a
    consistent way. doesn't do any error checking, so empty strings are not
    illegal, but will produce crummy filenames

    the format of the path is
    <directory>/<year>/<datatype>_<year>-<month>.json

    Args:
        directory: the directory under which the file will be created
        year: the integer year to append, will expand to four digits if fewer,
              does not validate
        month: the integer month to append, will expand to two digits if fewer,
               does not validate
        data: a JSON serializable data structure
        datatype: the root of the filename

    Returns:
        The path to the file that was created
    """
    filename = get_monthly_file_path(directory, datatype, year, month)
    __dump_json_file(filename, data)
    return filename


def dump_to_daily_json_file(directory, year, month, day, data, datatype=''):
    """saves data to a daily file stored in JSON

    this function will create the directories if needed and will set up the
    filename in a consistent way (using the get_daily_file_path method).
    the format is of the structure
    <directory>/<year>/<year>-<month>-<day>/<datatype>.<file_extension>

    Args:
        directory: the directory under which the path to the day is created
        year: the integer year to append, will expand to four digits if fewer,
              does not validate
        month: the integer month to append, will expand to two digits if fewer,
               does not validate
        day: the integer day to append, will expand to two digits if fewer,
             does not validate
        data: a JSON serializable data structure
        datatype: the root of the filename

    Returns
        The path to the filename that was created
    """
    filename = get_daily_file_path(directory, datatype, year, month, day)
    __dump_json_file(filename, data)
    return filename


def find_newest_saved_month(directory, end_year, datatype=''):
    """finds the last saved file for data stored by month

    walks backwards in time starting from the current date looking for the last
    saved data by month

    Args:
        directory: the directory under which to look
        end_year: the year to end at
        datatype: the root of the filename

    Returns:
        The year and month of the last saved file, if end_year is reached,
        None, None is returned
    """
    check_date = datetime.datetime.now()
    done = False

    if os.path.isdir(directory):
        while not done:
            if os.path.exists(get_monthly_file_path(directory, datatype,
                              check_date.year, check_date.month,
                              make_directories=False)):
                return check_date.year, check_date.month
            check_date = check_date - dateutil.relativedelta.relativedelta(
                months=1)
            if check_date.year <= end_year:
                done = True

    return None, None
