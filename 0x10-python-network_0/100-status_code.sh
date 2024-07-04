#!/bin/bash
# Sends a request to a URL and displays only the status code
curl -o /dev/null -s -w "%{http_code}" "$1"
