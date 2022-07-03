import datetime


def validate_date_format(date):
    """
    Function to validate if a date has a structure dd-mm-yyyy
    :param date: str a date
    :return bool: True if the date has the right structure
    """
    try:
        datetime.datetime.strptime(date, "%d-%m-%Y")
        return True
    except:
        return False


def get_valid_date_format(date):
    """
    Function to add H:M:S to a date
    :param date: a previously validated date
    :return str: A date with the structure yyy-mm-dd H:M:S
    """
    date_object = datetime.datetime.strptime(date, "%d-%m-%Y")
    return date_object.strftime("%Y-%m-%d %H:%M:%S")


def get_timestamp_object(timestamp):
    """
    Function to cast a str with the structure yyy-mm-dd H:M:S
    :param timestamp: a date with structure yyy-mm-dd H:M:S
    :return timestamp_object: a datetime object or None if the timestamp has wrong structure
    """
    try:
        timestamp_object = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        return timestamp_object
    except:
        return None
