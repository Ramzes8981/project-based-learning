# minidbg-c — рабочий README

## Scope

```text
Linux x86-64
single-threaded controlled tracees
launch only (no arbitrary attach in core)
```

## Build / targets

Document debugger build and use `tests/targets/Makefile` to build controlled fixtures.

## State machine

List debugger states and commands allowed from each state. Every `waitpid` result must transition explicitly.

## Tracee ownership/lifecycle

Who creates child, what happens on debugger quit, detach/terminate policy, zombie prevention.

## Registers/memory

Address parser, errno handling for PEEK, architecture-specific assumptions.

## Breakpoints

Record layout, insertion/deletion, duplicate policy, hit detection, RIP correction, step-over/reinsert state.

## PIE

How runtime mapping base + symbol relative value become runtime breakpoint address. Include evidence for one PIE fixture.

## Tests

`TESTS.md`, controlled targets, expected stops/register effects. Never test by attaching to unrelated user/system processes.

## Security/non-goals

This is a debugging learning tool, not an exploitation framework. No untrusted remote attach, no anti-debug bypass, no stealth/injection features.

## Debugging story / known limitations / transfer

