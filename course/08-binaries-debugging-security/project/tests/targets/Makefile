CC ?= cc
CFLAGS := -std=c17 -Wall -Wextra -Wpedantic -g

.PHONY: all clean

all: basic-nopie loop-nopie stack-fp stack-opt basic-pie signal

basic-nopie: target_basic.c
	$(CC) $(CFLAGS) -O0 -fno-pie -no-pie $< -o $@

loop-nopie: target_loop.c
	$(CC) $(CFLAGS) -O0 -fno-pie -no-pie $< -o $@

stack-fp: target_stack.c
	$(CC) $(CFLAGS) -O0 -fno-omit-frame-pointer -fno-pie -no-pie $< -o $@

stack-opt: target_stack.c
	$(CC) $(CFLAGS) -O2 -fomit-frame-pointer -fno-pie -no-pie $< -o $@

basic-pie: target_basic.c
	$(CC) $(CFLAGS) -O0 -fPIE -pie $< -o $@

signal: target_signal.c
	$(CC) $(CFLAGS) -O0 -fno-pie -no-pie $< -o $@

clean:
	rm -f basic-nopie loop-nopie stack-fp stack-opt basic-pie signal
