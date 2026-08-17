# Tiny16 — Hints

## Hint 1

Сначала реализуй encode/decode **одной** instruction и tests, не весь parser.

## Hint 2

Emulator state и decoded instruction — разные structs/concepts. Это помогает не смешивать parse bits и mutation.

## Hint 3

Assembler pass 1 знает addresses labels; pass 2 знает их значения при encode.

## Hint 4

Для signed imm9 сначала определи допустимый математический range, затем encode low 9 bits осознанно.

## Hint 5

Branch bugs удобнее всего ловить trace таблицей `PC before -> instruction -> PC after`.
