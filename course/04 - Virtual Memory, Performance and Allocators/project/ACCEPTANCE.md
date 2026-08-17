# Arena Allocator — Acceptance

## Stage 1

- valid alignments return correctly aligned pointers;
- invalid alignment rejected;
- exact-end fit succeeds if policy allows;
- one-byte-too-large fails without state mutation;
- all size/offset addition/multiplication checked before pointer arithmetic;
- zero-size policy tested.

## Stage 2

- freed block reusable;
- split remainder remains valid/free;
- adjacent free blocks coalesce;
- nonadjacent blocks never coalesce merely because list neighbors;
- invalid interior/outside pointer rejected;
- double free rejected/no metadata damage;
- full free cycle can recover large block where coalescing should permit it.

## Resource/safety

- arena ownership/destroy contract explicit;
- no OOB/UAF/double system free under sanitizers;
- warning-clean build;
- failure leaves allocator inspectable/destructible.

## Evidence

- fragmentation metrics have definitions;
- one policy workload comparison;
- debugging story;
- transfer feature/decision.