#!/bin/bash
# Displays the size of the response body in bytes

curl -sL "$1" | wc -c
