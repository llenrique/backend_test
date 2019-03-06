u"""

"""
import os
import requests
import json


def host():
    return os.environ.get('APIURL')


def make_request(method, uri, json=None):
    path = '{}/{}'.format(host(), uri)
    try:
        response = requests.request(method, path, json=json)
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
        res = r.headers['content-type']
        if res == "application/json; charset=utf-8":
            return r.json()
        else:
            return r.text
    except json.decoder.JSONDecodeError as j:
        print('Error: {}'.format(j))
