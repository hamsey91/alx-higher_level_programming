#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""
from requests import get
from sys import argv


if __name__ == '__main__':

    username = argv[1]
    password = argv[2]

    request_url = "https://api.github.com/user"
    response = get(request_url, Auth=(username, password))
    print(response.json().get('id'))
