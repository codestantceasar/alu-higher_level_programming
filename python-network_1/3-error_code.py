#!/usr/bin/python3
"""Sends a request to a URL and displays the body or error code."""

import urllib.request
import urllib.error
import sys


def main():
    """Handle the HTTP request and response."""
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            # If the request is successful (status code 200)
            print("Regular request")
    except urllib.error.HTTPError as e:
        # If an HTTP error occurs, print the error code
        print(f"Error code: {e.code}")
    except urllib.error.URLError as e:
        # Handle other URL-related errors (e.g., connection refused)
        print(f"URL Error: {e.reason}")


if __name__ == "__main__":
    main()
