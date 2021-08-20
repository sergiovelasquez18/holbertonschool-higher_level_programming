#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
        print(html.decode("utf-8"))
    except urllib.error.HTTPError as error_code:
        print("Error code: {}".format(error_code.code))
