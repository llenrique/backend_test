u"""

"""
import os
import requests


def host():
    return os.environ.get('APIURL')


def service_request(method, uri, json=None):
    path = '{}/{}'.format(host(), uri)
    print("{}".format(path))
    try:
        response = requests.request(method, path, json=json)
        if response.status_code == 200:
            return response
        elif response.status_code == 406:
            return response.status_code
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
