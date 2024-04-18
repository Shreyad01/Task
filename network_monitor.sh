#!/bin/bash

TARGET_IP="8.8.8.8"

ALERT_THRESHOLD=3


LOG_FILE="/Desktop/Practice/Task1/network_monitor.log"


log() {
    local timestamp=$(date +"%d-%m-%Y %T")
    echo "[$timestamp] $1" >> "$LOG_FILE"
}


send_alert() {
    local message="Network connectivity issue: $1"
    echo "$message"
    
}

monitor_network() {
    local consecutive_fails=0

    while true; do
        if ping -c 1 "$TARGET_IP" > /dev/null 2>&1; then
            
            consecutive_fails=0
            log "Ping to $TARGET_IP successful."
        else
            
            ((consecutive_fails++))
            log "Ping to $TARGET_IP failed. Consecutive fails: $consecutive_fails"

            if ((consecutive_fails >= ALERT_THRESHOLD)); then
                send_alert "Consecutive ping failures reached $ALERT_THRESHOLD."
            fi
        fi
        sleep 60
    done
}
monitor_network

