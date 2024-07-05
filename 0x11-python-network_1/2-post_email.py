#!/usr/bin/python3
"""
Script that sends a POST request with the email as parameter
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':

    request_url = sys.argv[1]
    e_mail = sys.argv[2]
    data = urllib.parse.urlencode({"email": e_mail})
    data = data.encode('ascii')

    with urllib.request.urlopen(request_url, data) as response:
        print(response.read().decode('utf-8'))
