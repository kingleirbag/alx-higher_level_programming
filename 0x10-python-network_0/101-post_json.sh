#!/bin/bash
# Sends a JSON POST request to a URL passed and display body response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
