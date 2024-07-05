#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
It then handles the JSON response according to the specified requirements
"""
import requests
import sys

if __name__== "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": q}
    try:
        response = requests.post(url, data=payload)
        json_response = response.json()
        if json_response and isinstance(json_response, dict):
            if 'id' in json_response and 'name' in json_response:
                print("[{}] {}".format(json_response['id'], json_response['name']))
            else:
                print("No result")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
