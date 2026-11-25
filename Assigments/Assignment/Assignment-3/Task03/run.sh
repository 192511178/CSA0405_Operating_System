#!/bin/sh
set -eu
gcc -std=c11 -Wall -Wextra segments.c -o segments
gcc -std=c11 -Wall -Wextra segfault_demo.c -o segfault_demo
./segments
./segfault_demo
python3 segmentation_experiments.py
