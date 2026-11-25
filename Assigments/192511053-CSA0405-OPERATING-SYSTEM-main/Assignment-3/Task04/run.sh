#!/bin/sh
set -eu
gcc -std=c11 -Wall -Wextra vm_experiment.c -o vm_experiment
gcc -std=c11 -Wall -Wextra access_patterns.c -o access_patterns
./vm_experiment 64
./access_patterns
python3 vm_eat.py
python3 frame_fault_plot.py
