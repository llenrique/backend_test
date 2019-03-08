"""Retrives a response and try to retrn a json or a text."""

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
