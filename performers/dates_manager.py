from datetime import datetime


def set_date(date_name):
    """
    Indicate the user to type a date with one format and validates the input.

    Then return a datetime object
    """
    date = input('Give me the {} date (FORMAT YYYY-MM-DD): '.format(date_name))
    date = date_validate(date)
    if date is False:
        date = set_date(date_name)
    return date


def date_validate(date):
    """
    Return the string-date value to validate with the required date format.

    If the string-date value can be converted to an datetime object with the
    given format the function returns the converted date.

    Else return false value to indicates that the string has the incorrect
    format.

    Example:
        With the format %Y-%m-%d and the string-date value 2017-01-01
        the returned value will be an date object with the format YYYY-mm-dd.

        But with the string-date value 217-01-01 the conversion cannot be done,
        so the function will return False
    """
    try:
        format_str = '%Y-%m-%d'
        if datetime.strptime(date, format_str):
            date = datetime.strptime(date, format_str)
            return date.date()
    except Exception as e:
        print("Error")
        print(e)
        return False
