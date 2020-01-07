#!/usr/bin/env bash
set -e
docker build . -t gedi-pub
docker run -d -p 1883:1883 --name gedi-pub --rm gedi-pub
