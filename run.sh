#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: ./run.sh /path/to/places.sqlite"
    exit 1
fi

TIMESTAMP="$(date '+%Y%m%d%H%M%S')"
COPY="/tmp/${TIMESTAMP}_places.sqlite"
cp "$1" "$COPY"
python3 ./main.py "$COPY"

