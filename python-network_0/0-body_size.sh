#!/bin/bash

# Check if the URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the size of the response body using curl and Content-Length
size=$(curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}')

# Check if the size is available and display #
if [ -n "$size" ]; then
  printf '#%.0s' $(seq 1 "$size")
  echo
else
  echo "Error: Could not retrieve Content-Length"
fi
