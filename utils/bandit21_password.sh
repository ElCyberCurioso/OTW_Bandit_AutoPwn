#!/bin/bash

# Variables
PASS="$1"
PORT=4444
OUTFILE="$2"

# Temporary folder
WORKDIR="$3"
cd "$WORKDIR"

# Deploy listener and send password
( echo "$PASS" | nc -nlvp "$PORT" > "$OUTFILE" ) &

# Wait until nc is ready
sleep 1

# Execute suconnect
/home/bandit20/suconnect "$PORT"

# Wait until it ends
sleep 1

# Show result
cat "$OUTFILE"