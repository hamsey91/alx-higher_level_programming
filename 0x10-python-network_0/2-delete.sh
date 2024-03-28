#!/bin/bash
# Script that sends a DELETE request to the URL as first argument and displays the body.
curl -s "$1" -X DELETE
