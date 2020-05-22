import os
import time
import dateutil
import datetime

def get_monthly_filename(directory, file_prefix, file_extension, year, month):
    return os.path.join(directory, '{}-{:04d}-{:02d}.{}'.format(file_prefix, year, month, file_extension))


def format_monthly_json_filename(year, month, datatype=''):
    datatype_str = ''
    if len(datatype) > 0:
        datatype_str = f'{datatype}_'
    return f'{datatype_str}{year}-{month:02}.json'


def dump_to_monthly_json_file(data_directory, year, month, data, datatype=''):
    directory = os.path.join(data_directory, str(year))
    if not os.path.isdir(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, format_monthly_json_filename(year,month,datatype))
    with open(filename, "w") as f:
        f.write(json.dumps(data, indent=2))
    time.sleep(1)


def find_newest_saved_month(data_directory, end_year, datatype=''):
    check_date = datetime.datetime.now()
    done = False

    if os.path.isdir(data_directory):
        while not done:
            if os.path.isdir(os.path.join(data_directory, str(check_date.year))):
                if os.path.exists(os.path.join(data_directory, str(check_date.year), format_monthly_json_filename(check_date.year, check_date.month, datatype))):
                    return check_date.year, check_date.month
            check_date = check_date - dateutil.relativedelta.relativedelta(months=1)
            if check_date.year <= end_year:
                done = True
    
    return None, None
