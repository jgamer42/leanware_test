import datetime


def validate_date_format(date):
    try:
        date_object = datetime.datetime.strptime(date, "%d-%m-%Y")
        return True
    except:
        return False


def get_valid_date_format(date):
    date_object = datetime.datetime.strptime(date, "%d-%m-%Y")
    return date_object.strftime("%Y-%m-%d %H:%M:%S")


def get_timestamp_object(timestamp):
    try:
        timestamp_object = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        return timestamp_object
    except:
        return None
