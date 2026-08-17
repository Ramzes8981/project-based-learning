# Rust MiniKV — staged SPEC

## Prerequisites

Start implementation after 1B.6. FFI and concurrency are not prerequisites.

## Behavior

- insert new `String` key/value or integer value according to chosen model;
- update existing key without duplicate logical entry;
- lookup by borrowed key (`&str`) without allocating a temporary owned key;
- delete returns explicit found/not-found semantics;
- length remains correct.

## Ownership contract

Store owns inserted keys and values. Caller may borrow returned data only for lifetime allowed by Rust API. Mutation that requires `&mut self` cannot overlap incompatible borrows.

## Error/absence model

Use `Option` for ordinary missing lookup where appropriate. Use `Result` only for actual failure category that has meaningful error information; do not wrap every operation in `Result` by ritual.

## Clone policy

A clone is acceptable only when semantic result requires a new independent owner. README must explain any clone on hot lookup/update path.

## Safety

Core project uses safe Rust. Adding `unsafe` to bypass borrow checker is not an accepted solution.

## Transfer task

Add one API that returns a borrowed view, then explain its lifetime relationship in words before code.