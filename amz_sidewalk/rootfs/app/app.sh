#!/usr/bin/env bash

# Effacer l'écran
clear

# Start main.py in background
python3 /app/main.py &

# Start app.sh in foreground
while true
do
    sh /app/app.sh &
    sleep 3 &
    echo "bash script" &
    sleep 3

    # Effacer l'écran
    clear
done
