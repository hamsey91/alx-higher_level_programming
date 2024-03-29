#!/usr/bin/python3
"""
Script that sends a request to the URL,
and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":

    data = {'q': argv[1] if len(argv) >= 2 else ""}
    req = post('http://0.0.0.0:5000/search_user', data)

    t_req = req.headers['content-type']

    if t_req == 'application/json':
        res = req.json()
        s_id = res.get('id')
        s_name = res.get('name')
        if (res != {} and s_id and s_name):
            print("[{}] {}".format(s_id, s_name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
