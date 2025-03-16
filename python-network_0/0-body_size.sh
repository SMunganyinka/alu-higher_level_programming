#!/bin/bash

url="$1"

if [[ -z "$url" ]]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

body_size=$(curl -s "$url" | wc -c)

echo "$body_size"
