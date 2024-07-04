#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Sends a GET request to the URL and displays the body of a 200 status
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
