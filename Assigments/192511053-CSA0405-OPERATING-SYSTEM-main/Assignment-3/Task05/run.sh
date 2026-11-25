#!/bin/sh
set -eu
gcc -std=c11 -Wall -Wextra replacement.c -o replacement
./replacement
python3 replacement_experiments.py
