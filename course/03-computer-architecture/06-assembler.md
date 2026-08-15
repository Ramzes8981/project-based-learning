# 3.6 — Assembler и symbol table

**Теория:** ~65 мин  
**Project slice:** ~4–7 часов  
**С телефона:** теория — да

← [`05-fetch-decode-execute.md`](05-fetch-decode-execute.md) · → [`07-x86-64-abi-bridge.md`](07-x86-64-abi-bridge.md)

## Цель

Построить two-pass assembler и применить hash-table/symbol-table знания Module 1.

## Почему two pass

Assembly может содержать forward label:

```asm
JMP end
...
end:
HALT
```

На первой строке assembler ещё не знает address `end`, если код читается сверху вниз.

### Pass 1

- tokenize/parse lines;
- считать instruction addresses;
- записать labels → addresses в symbol table;
- не emit final words для labels.

### Pass 2

- снова пройти instructions;
- resolve symbol operands;
- validate ranges;
- encode machine words.

## Parser boundaries

Не строй сложный compiler frontend. Course assembly grammar ограничен:

```text
optional label
mnemonic
comma/whitespace-separated operands
optional comment
```

## Error quality

Assembler должен сообщать:

- line number;
- unknown mnemonic;
- wrong operand count/type;
- duplicate label;
- unknown label;
- immediate/target out of range.

Хорошие diagnostics — инженерная часть project, а не украшение.

## Symbol table

Ты уже реализовал hash table. Можно:

- повторно использовать собственную;
- либо для scope assembler использовать simpler structure, если это уменьшает irrelevant work.

Решение должно быть осознанным.

## Project slice

Заверши assembler и создай sample programs:

- arithmetic;
- loop sum;
- memory load/store;
- conditional branch;
- invalid-input fixtures.

Output — deterministic binary/hex words, которые принимает emulator.

## Exit check

Объясни, почему forward labels естественно приводят к two-pass design.
