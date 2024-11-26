#!/usr/bin/python3
"""Sends a request to a URL and displays the body or error code."""

import urllib.request
import urllib.error
import sys


def main():
    """Main function to handle the HTTP request and response."""
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    req = urllib.request.Request(url)
    
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")


if __name__ == "__main__":
    main()
