# 8.8 — Memory corruption и exploit mitigations bridge

**Теория:** ~100 мин  
**Local lab:** ~90 мин  
**С телефона:** теория — да

← [`07-dwarf-source-debugging.md`](07-dwarf-source-debugging.md) · → [`09-module-checkpoint.md`](09-module-checkpoint.md)

## Цель

Связать C memory bugs с runtime consequences и понять mitigations без перехода к атаке реальных систем.

## Memory corruption classes recap

- stack/heap out-of-bounds write;
- use-after-free;
- double free;
- integer overflow → undersized allocation;
- format/string parsing bugs;
- uninitialized data.

Bug и exploitability — разные вещи. Многие bugs crash, leak data or are non-exploitable under context; некоторые дают control primitives.

## NX / W^X

No-eXecute memory permissions запрещают execution из writable data pages like normal stack/heap under policy.

Это мешает классическому injected-code execution, но не предотвращает overwrite/corruption itself и не запрещает code-reuse attacks.

## Stack canary

Compiler вставляет guard value между certain local stack buffers/control metadata. Epilogue checks corruption and aborts if canary changed.

Canary ловит часть sequential stack overwrites, но:

- не предотвращает heap corruption;
- не гарантирует любой overwrite;
- detection happens when check executes.

## ASLR + PIE

Randomizes runtime addresses, снижая predictability. Information leak может weaken it; non-memory bugs remain.

## RELRO

Relocation Read-Only hardening makes selected dynamic-linker metadata read-only after relocation. Full/partial details depend linker flags/runtime.

It narrows writable control data surface, but not general memory safety.

## Fortification / sanitizers

Build hardening (`_FORTIFY_SOURCE`, stack protector etc.) и sanitizers имеют разные goals:

- hardening production consequences/detection;
- sanitizers development diagnostics with overhead.

Не ship ASan как universal production mitigation by assumption.

## Local lab

Controlled toy only:

```c
void copy_bad(const char *src) {
    char buf[16];
    /* deliberately unsafe boundedness bug for diagnosis */
}
```

Lab goals:

1. reproduce crash/canary diagnostic with oversized local test input;
2. inspect stack/mappings in GDB/minidbg;
3. compile with/without stack protector in isolated toy to compare detection;
4. inspect ELF hardening attributes/mappings where tooling available;
5. fix root cause with explicit bounds.

No remote target, privilege escalation or weaponized payload.

## Defense-in-depth

```text
memory-safe design/language
+ bounds/ownership correctness
+ compiler hardening
+ ASLR/NX/RELRO
+ least privilege/sandbox
+ testing/fuzzing/sanitizers
```

Mitigations buy defense layers, not permission to leave UB.

## Rust bridge

Safe Rust prevents many spatial/temporal memory-safety classes through bounds/ownership checks. `unsafe` Rust/FFI can reintroduce them; logical/protocol bugs remain.

## Causal questions

1. Почему NX не чинит buffer overflow?
2. Почему ASLR не помогает, если attacker already leaks exact addresses?
3. Почему canary не защищает heap?
4. Как Rust reduces attack surface without solving authorization/protocol design?

## Exit check

Для каждого mitigation назови конкретный assumption/class attack it complicates и что остаётся unprotected.
