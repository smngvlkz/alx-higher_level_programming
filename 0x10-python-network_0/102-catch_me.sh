#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the serveer to respond with a message
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
