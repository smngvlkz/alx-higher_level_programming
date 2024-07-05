#!/usr/bin/python3
# Takes in a URL and an email and sends a POST request to the passed URL with the email as a parameter. It also displays the body response"
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    req = urllib.request.Request(url, data=data)
    
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
