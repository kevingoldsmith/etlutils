import os
import time
import dateutil
import datetime
import json


# yearly file format {datadirectory/}name_YYYY{.extension}
# monthly file format {datadirectory/}YYYY/name_YYYY-MM{.extension}
# daily file format {datadirectory/}YYYY/YYYY-MM-DD/name{.extension}

def get_yearly_file_path(directory, datatype, year, file_extension='json', make_directories=True):
    if make_directories and (not os.path.exists(directory)):
        os.mkdir(directory)
    return os.path.join(directory, f'{datatype}_{year:04}.{file_extension}')


def get_monthly_file_path(directory, datatype, year, month, file_extension='json', make_directories=True):
    path = directory
    if make_directories and path and (not os.path.exists(path)):
        os.mkdir(path)
    path = os.path.join(path, f'{year:04}')
    if make_directories and (not os.path.exists(path)):
        os.mkdir(path)
    return os.path.join(path, f'{datatype}_{year:04}-{month:02}.{file_extension}')


def get_daily_file_path(directory, datatype, year, month, day, file_extension='json', make_directories=True):
    path = directory
    if make_directories and path and (not os.path.exists(path)):
        os.mkdir(path)
    path = os.path.join(path, f'{year:04}')
    if make_directories and (not os.path.exists(path)):
        os.mkdir(path)
    path = os.path.join(path, f'{year:04}-{month:02}-{day:02}')
    if make_directories and (not os.path.exists(path)):
        os.mkdir(path)
    return os.path.join(path, f'{datatype}.{file_extension}')


def dump_to_monthly_json_file(data_directory, year, month, data, datatype=''):
    filename = get_monthly_file_path(data_directory, datatype, year, month)
    with open(filename, "w") as f:
        f.write(json.dumps(data, indent=2))
    time.sleep(1)


def find_newest_saved_month(data_directory, end_year, datatype=''):
    check_date = datetime.datetime.now()
    done = False

    if os.path.isdir(data_directory):
        while not done:
            if os.path.exists(get_monthly_file_path(data_directory, datatype, check_date.year, check_date.month, make_directories=False)):
                return check_date.year, check_date.month
            check_date = check_date - dateutil.relativedelta.relativedelta(months=1)
            if check_date.year <= end_year:
                done = True
    
    return None, None
