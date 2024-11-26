#!/usr/bin/python3
"""
Sends a GET request to a URL and displays the body of the response.

If the HTTP status code is >= 400, prints "Error code: <status_code>".

Usage:
    ./3-error_code.py <URL>
"""

import urllib.request
import urllib.error
import sys


def main():
    """
    Handle the HTTP GET request and process the response.

    Args:
        None

    Returns:
        None

    Prints:
        - The body of the response if the status code is 200.
        - "Error code: <status_code>" if the status code is >= 400.
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    main()
