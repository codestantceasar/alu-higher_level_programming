#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status and displays response info."""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status')respons:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
