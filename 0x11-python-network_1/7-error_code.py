#!/usr/bin/python3
# Takes in a URL, sends a request to the URL and displays the body of the response"
import requests
import sys

def fetch_url(url):
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        fetch_url(url)
