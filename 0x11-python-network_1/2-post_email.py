#!/usr/bin/python3
"""script that takes in a URL, sends a request to
the URL and displays the value of the X-Request-Id variable
found in the header
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(value).encode('utf-8')
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    request = urllib.request.Request(url, data, headers=headers, method='POST')

    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
