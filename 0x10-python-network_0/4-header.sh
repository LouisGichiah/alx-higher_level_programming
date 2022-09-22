#!/bin/bash
# takes in an URL as an argument, sends a GET request to the URL and displays the body of the response
curl -s "$1" -X GET -H "School-User-Id: 98"
