#!/usr/bin/env sh

cd "$(dirname "$0")/public" || exit 1
exec python3 -m http.server 8888
