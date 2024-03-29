#!/usr/bin/python3
"""
Script that sends a  request to URL,displays the body of the response
"""
import sys
import urllib.request
import urllib.error


if __name__ == '__main__':

    request_url = sys.argv[1]
    try:
        with request.urlopen(request_url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.status))
