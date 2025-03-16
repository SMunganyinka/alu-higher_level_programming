#!/bin/bash

# Check if the URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to send the request and display the size of the body of the response
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
