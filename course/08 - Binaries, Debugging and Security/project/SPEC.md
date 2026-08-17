# minidbg-c — SPEC

## Platform

- Linux;
- x86-64;
- single-threaded tracee core;
- C17 debugger implementation.

## Launch

```text
minidbg-c ./target [args...]
```

Debugger launches tracee through fork/TRACEME/exec path.

## Required commands

```text
continue / c
step / s
regs
reg NAME
mem ADDRESS
break ADDRESS
breaks
disable/delete breakpoint
quit
```

Exact command grammar student designs/documents.

## Breakpoints

- address breakpoints;
- save original byte;
- insert x86 `0xCC`;
- detect hit at expected address;
- restore + RIP correction + single-step + reinsert;
- duplicate breakpoint safe.

## State machine

Debugger must distinguish:

- running;
- stopped;
- breakpoint stop;
- single-step stop;
- other signal stop;
- exited;
- signaled termination.

## PIE

Core first passes non-PIE fixtures. Acceptance additionally requires documented runtime-address resolution for at least one PIE symbol/address using mapping base + known relative symbol value/tooling.

## Non-goals

- multithread debug;
- full source-level DWARF parser;
- hardware breakpoints;
- remote debugging;
- arbitrary untrusted process attach;
- production debugger UI.
