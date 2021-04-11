#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: ./run.sh /home/username/.mozilla/firefox/0xdeadbeef.default-release/places.sqlite"
    exit 1
fi

TIMESTAMP="$(date '+%Y%m%d%H%M%S')"
COPY="/tmp/places_${TIMESTAMP}.sqlite"
cp "$1" "$COPY"
./build.sh && docker run \
    -it \
    --rm \
    --name my-running-app \
    -v "$COPY":"/usr/src/app/places.sqlite" \
    firefox-bookmarks-wayback

