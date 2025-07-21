#!/bin/bash

function ctrl_c(){
  echo -e "\n\n[!] Exiting...\n"
  tput cnorm; exit 1
}

# Ctrl+C
trap ctrl_c INT

tput civis # Hide cursor
for port in $(seq 31000 32000); do
  (echo '' > /dev/tcp/127.0.0.1/$port) 2>/dev/null && echo "$port" &
done; wait

# Show cursor
tput cnorm
