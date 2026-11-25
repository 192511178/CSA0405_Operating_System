#!/bin/sh
set -eu
gcc -std=c11 -Wall -Wextra -fPIC -c crypto.c -o crypto.o
gcc -std=c11 -Wall -Wextra -c bank.c -o bank.o
gcc -static bank.o crypto.o -o bank_static
gcc -shared -o libcrypto_demo.so crypto.o
gcc bank.o -L. -lcrypto_demo -Wl,-rpath,'$ORIGIN' -o bank_dynamic
gcc -std=c11 -Wall -Wextra runtime.c -ldl -o runtime_loader
printf 'STATIC SIZE: '; stat -c %s bank_static
printf 'DYNAMIC SIZE: '; stat -c %s bank_dynamic
echo 'DYNAMIC DEPENDENCIES:'; ldd ./bank_dynamic
echo 'STATIC RUN:'; ./bank_static
echo 'DYNAMIC RUN:'; ./bank_dynamic
echo 'RUNTIME LOAD:'; ./runtime_loader
echo 'MISSING LIBRARY TEST:'
./runtime_loader ./missing.so || true
echo 'STARTUP TIMING:'
/usr/bin/time -f 'static elapsed=%e s maxrss=%M KB' ./bank_static >/dev/null
/usr/bin/time -f 'dynamic elapsed=%e s maxrss=%M KB' ./bank_dynamic >/dev/null
