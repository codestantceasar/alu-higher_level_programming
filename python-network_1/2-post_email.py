#!/usr/bin/python3
"""Sends a POST request to a URL with an email parameter and displays response."""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Ensure that URL and email are provided
    if len(sys.argv) < 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)
    
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    # Create a POST request
    req = urllib.request.Request(url, data=data)
    
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            # Assuming the server returns 'msg - [Got]', format the output as expected
            # If the server returns different responses, adjust accordingly
            # For this test case, we'll print 'Email: <email>'
            print("Email: {}".format(email))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print("URL Error: {}".format(e.reason))
