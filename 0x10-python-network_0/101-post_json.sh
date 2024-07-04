#!/bin/bash
# Script that sends a JSON POST request and displays if the JSON is valid or not
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1" | grep -q "Valid JSON" && echo "Valid JSON" || echo "Not a valid JSON"
