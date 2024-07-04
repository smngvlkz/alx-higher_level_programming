#!/bin/bash
# Displays all HTTP methods the server will accept for a given URL
curl -sI "$1" | grep -i "^Allow:" | sed 's/^Allow: //'
