# Tiny16 — Acceptance

- every documented opcode has tests;
- assembler round-trips known encodings;
- labels forward/backward work;
- immediate/target ranges validated;
- invalid opcode -> controlled error;
- invalid PC/memory access -> controlled error according to spec;
- trace contains PC/raw word/decoded op or equivalent useful state;
- sample loop program executes correctly;
- sanitizer-clean host C implementation;
- no unexplained warnings;
- README explains ISA vs emulator implementation;
- transfer feature.
