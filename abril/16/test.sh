#!/bin/sh


rm -f teste_collatz
gcc -std=c99 -I. -Wall collatz.c teste_collatz.c -o teste_collatz  # && clear && \
./teste_collatz
