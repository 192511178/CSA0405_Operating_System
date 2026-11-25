#!/bin/sh
set -eu
gcc -std=c11 -Wall -Wextra paging.c -o paging
gcc -std=c11 -Wall -Wextra paging_2k.c -o paging_2k
echo 'PAGE SIZE 1024'; ./paging
echo 'PAGE SIZE 2048'; ./paging_2k
python3 paging_experiments.py
