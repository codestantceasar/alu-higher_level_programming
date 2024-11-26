#!/usr/bin/python3
"""
# A Python script that fetches http://0.0.0.0:5050/status using urllib

import urllib.request

# URL to be fetched
url = "http://0.0.0.0:5050/status"

# Using urllib to send a request to the URL and fetch its response
with urllib.request.urlopen(url) as response:
    # Read the response body
    body = response.read()
    
    # Print details about the response body
    print("Body response:")
    print("\t- type: {}".format(type(body)))  # Print the type of the response content
    print("\t- content: {}".format(body))      # Print the raw content of the response
    print("\t- utf8 content: {}".format(body.decode('utf-8')))  # Print the response content decoded as UTF-8
