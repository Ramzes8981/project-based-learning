# 8.6 — Single-step и пределы stack unwinding

**Теория:** ~80 мин  
**Project slice:** ~4–6 часов  
**С телефона:** да

← [`05-software-breakpoints.md`](05-software-breakpoints.md) · → [`07-dwarf-source-debugging.md`](07-dwarf-source-debugging.md)

## Цель

Использовать instruction single-step и понимать, почему RBP-chain — только учебный special case unwinding.

## `PTRACE_SINGLESTEP`

Restart request запускает stopped tracee и просит остановить его после следующей machine instruction (учитывая возможные signal/tracing events). Сам `ptrace` call возвращает после restart request; tracer узнаёт новый stop только через последующий `waitpid`.

```text
STOPPED
 -> PTRACE_SINGLESTEP
 -> RUNNING
 -> waitpid
 -> STOPPED/EXITED/SIGNALED
```

Это тот же state-machine discipline, который нужен breakpoint step-over.

## Frame-pointer model

При `-O0 -fno-omit-frame-pointer` и обычном x86-64 calling convention часто можно наблюдать chain:

```text
RBP -> previous RBP
RBP+8 -> return address
```

Но это compiler/code-generation convention under assumptions, не C language guarantee.

Compiler может omit frame pointer, inline, tail-call, rearrange prologue/epilogue или represent optimized frames иначе.

## Bounded educational walk

Stretch `bt` может:

1. start current RBP;
2. validate alignment/mapping/read success;
3. read previous RBP + return address;
4. require monotonic/sane stack direction/range under target assumptions;
5. cap maximum frames;
6. stop on zero/error/cycle/sanity violation.

Нельзя бесконечно chase arbitrary tracee values as pointers.

## Real unwind metadata

Production debuggers use ABI rules + unwind metadata such as DWARF Call Frame Information, not blind frame-pointer chains. Lesson 8.7 объясняет source/debug metadata conceptually; full unwinder remains stretch.

## Project slice

Core `step`: show RIP before/after and decode resulting state. Stretch `bt`: only fixtures built with documented frame-pointer flags.

## Exit check

Почему successful `PTRACE_SINGLESTEP` request не означает, что tracee уже снова stopped?
