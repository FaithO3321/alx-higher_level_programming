#!/bin/bash
# Check if the URL argument is provided
curl -s -o /dev/null -w "%{http_code}" "$1"
