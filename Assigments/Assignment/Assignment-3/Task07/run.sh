#!/bin/sh
set -eu
gcc -std=c11 -Wall -Wextra locked_memory.c -o locked_memory
echo 'UNLOCKED'; ./locked_memory unlocked || true
echo 'LOCKED'; ./locked_memory lock || true
python3 memory_simulation.py
