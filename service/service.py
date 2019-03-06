u"""

"""
import os
import requests
import json


def host():
    return os.environ.get('APIURL')


def make_request(method, uri):
    path = '{}/{}'.format(host(), uri)
    try:
        response = requests.request(method, path)
        if response.status_code == 200:
            print("{}  Success API call ".format(path))
            return parse_json(response)
        elif response.status_code == 406:
            return False
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))


def parse_json(r):
    try:
        return r.json()
    except json.decoder.JSONDecodeError as j:
        print('Error: ')
        print(j)
