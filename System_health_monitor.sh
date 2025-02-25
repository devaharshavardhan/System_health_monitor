#!/bin/bash

# this is log file path
LOG_FILE="/home/ubuntu/system_health.log"

# This gets current date and time
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# This gets the CPU usage (average over 1 second) of instance.
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8"%"}')

# This gets memory usage of instance
MEM_USAGE=$(free | awk '/Mem/ {printf "%.2f%%", $3/$2 * 100}')

# This get disk_usage of instance
DISK_USAGE=$(df -h --output=pcent / | tail -1 | tr -d ' ')

# appending into log file
echo "$DATE - CPU: $CPU_USAGE, Memory: $MEM_USAGE, Disk: $DISK_USAGE" >> "$LOG_FILE"
