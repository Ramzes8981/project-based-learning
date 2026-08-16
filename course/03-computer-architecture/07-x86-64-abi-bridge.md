# 3.8 — Как отдельно скомпилированные функции договариваются о calls

**Теория:** ~90 мин · **Лаб:** ~90 мин · **С телефона:** theory — да

← [`06-assembler.md`](06-assembler.md) · → [`08-module-checkpoint.md`](08-module-checkpoint.md)

## Проблема

C compiler compiles `caller.c` and `callee.c` separately, linker joins them. But machine code still must agree:

```text
where arguments are?
where return value goes?
which registers callee must preserve?
how stack is aligned?
how function returns?
```

That shared binary calling contract is part of an **Application Binary Interface (ABI)**.

## ISA vs ABI

ISA says what instructions/registers mean. ABI says how software components use them together: calling convention, type/layout details, object format conventions and more.

Same ISA can support multiple ABIs.

## x86-64 System V course target

On typical Linux x86-64 SysV ABI, first integer/pointer args use registers such as `RDI, RSI, RDX, RCX, R8, R9`; integer return uses `RAX`. Some registers are caller-saved, others callee-saved; stack alignment has specific rules.

These are target-specific facts, not universal “x86-64 language rules”. Course lab verifies current target with compiler-generated assembly and debugger.

## Call stack now becomes concrete

Earlier call stack was lifetime mental model. ABI now explains one target-level mechanism: calls may use stack for return address, spilled registers, locals, extra arguments, alignment.

Compiler may optimize frames away/in-line functions; source-level local variable ≠ guaranteed stack slot.

## Observe, do not memorize blindly

Compile small C functions with debug/no-optimization and inspect:

```bash
cc -std=c17 -O0 -g -S sample.c -o sample.s
```

Then compare to optimized build. Ask which differences preserve same C/ABI observable behavior.

## FFI connection

Rust `extern "C"` asks for C ABI calling convention/layout contract on target. That is why FFI correctness depends on ABI-compatible types and `repr(C)`.

## Exit check

Why can two source files both compile correctly yet still interoperate incorrectly if they disagree on ABI signature/layout?