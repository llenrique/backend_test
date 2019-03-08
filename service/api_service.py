"""
Construct the endpoint and make GET or POST request.

First get the APIURL from the os (see README.md for know how to export it).
Then, make a request with the method and the builded uri. For POST method
a json param is needed. Then return the response of the previous request

Example
    service_request('GET', 'users/:start/:end', json=None)
    path = host() and concat the uri:'users/:start/:end'
    then make a request to the path with GET method and no json
    If the request has success
        return the response
    else if
        return the status_code
    else
        raise for status for handle Exceptions

"""
import os
import requests


def host():
    """Get the system environment APIURL variable"""
    return os.environ.get('APIURL')


def service_request(method, uri, json=None):
    """Construct path and make request"""
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
