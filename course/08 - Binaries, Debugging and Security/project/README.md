# minidbg-c — Linux x86-64 teaching debugger

Build a debugger for **course-owned fixtures only**. Target scope is deliberately narrow so every state transition remains explainable.

## Milestones

1. launch tracee + wait/continue/exit state machine;
2. register dump;
3. safe byte-range memory read/write helper;
4. software breakpoint table;
5. breakpoint hit dance: restore → RIP rewind → single-step → reinsert;
6. explicit `step` command;
7. frame-pointer-only stack trace on fixture built with frame pointers;
8. optional supported PIE symbol resolution.

## Non-goals

- remote debugging;
- arbitrary hostile process attachment;
- full DWARF parser;
- optimized universal unwinder;
- multi-threaded debugger completeness;
- exploit automation.

Docs: [`SPEC.md`](SPEC.md) · [`ACCEPTANCE.md`](ACCEPTANCE.md) · [`TESTS.md`](TESTS.md) · [`HINTS.md`](HINTS.md).