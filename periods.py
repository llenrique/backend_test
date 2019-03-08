"""Manage periods of time."""

from datetime import timedelta
from service import api_service
import json


def parse_json(r):
    try:
        res = r.headers['content-type']
        if res == "application/json; charset=utf-8":
            return r.json()
        else:
            return r.text
    except json.decoder.JSONDecodeError as j:
        print('Error: {}'.format(j))


def period_divisor(start_date, end_date, point):
    """
    Retrive a period of time and an api point (users/movements).

    if the service return a json object with the start and end dates given,then
    the function return those values (for users or movements).

    Else, the service cannot get the information between the start and
    end dates. So the period is divided by the half and try to get the info
    again whit this half of period.

    Example:
        With the given dates start: 2018-01-01 and end: 2018-07-02 the
        status code on the api call is a 406. So this period of time is
        divided by the half using the rounded days difference between this
        dates divided by 2, then, this result is added to the start date
        updating the params as start: 2018-01-01 end: 2018-04-02 for
        the firt-half of the initial period of time. For the second-half,
        is taken the end date of the first-half and add one day to avoid
        getting the same results of the same end date of the firt-half
    """
    uri = "{}/{}/{}".format(point, start_date, end_date)
    try:
        info = api_service.service_request('GET', uri)
        if info == 406:
            # print("Dividing path")
            diff = end_date - start_date
            days_control = round(diff.days / 2)
            first_half = [start_date, start_date + timedelta(days_control)]
            second_half = [start_date + timedelta(days_control+1), end_date]
            info = period_divisor(first_half[0], first_half[1], point)
            info += period_divisor(second_half[0], second_half[1], point)
        else:
            info = parse_json(info)
        return info
    except Exception as e:
        print("Error")
        print(e)
