# minidbg-c — Hints

## Hint 1

Сначала debugger с `continue` до exit. Breakpoints только после stable wait/state loop.

## Hint 2

Represent debugger state explicitly. Не выводи semantics только из последнего signal number.

## Hint 3

Breakpoint object = address + original byte + enabled. Patch operation отдельно от logical breakpoint record.

## Hint 4

При hit x86 `RIP` уже прошёл one-byte `INT3`; проверь breakpoint at `RIP-1` before correction.

## Hint 5

Step-over — temporary disabled breakpoint + one single-step + re-enable. Это state transition, не recursive `continue` hack.
