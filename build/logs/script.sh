#!/bin/bash


SCRIPT_PATH="/home/blackarch/syste/desk/poc.py"

# Filenames for profiling outputs
CPU_PROFILE="cpu_profile.stats"
MEMORY_PROFILE="memory_profile.log"
DISK_IO_LOG="disk_io.log"
NETWORK_LOG="network.log"


profile_cpu() {
    python -m cProfile -o $CPU_PROFILE $SCRIPT_PATH
}


profile_memory() {
    mprof run $SCRIPT_PATH
    mv 'mprofile*.dat' $MEMORY_PROFILE
}


monitor_disk_io() {
    sudo iotop -b -n 1 -o -qqq > $DISK_IO_LOG
}


monitor_network() {
    sudo iftop -t -s 1 > $NETWORK_LOG
}


profile_cpu &
profile_memory &


monitor_disk_io &
monitor_network &


wait


echo "CPU Profiling Results:"
pyprof2calltree -i $CPU_PROFILE -k


echo "Memory Profiling Results:"
mprof plot $MEMORY_PROFILE -o memory_profile.png
echo "Memory usage plot saved as memory_profile.png"


echo "Disk I/O Activity:"
cat $DISK_IO_LOG


echo "Network Traffic:"
cat $NETWORK_LOG

echo "Profiling Complete."
