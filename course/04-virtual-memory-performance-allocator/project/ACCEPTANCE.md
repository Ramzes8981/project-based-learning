# Arena Allocator — Acceptance

- create/destroy arena;
- many aligned allocations;
- exhaustion returns controlled failure;
- free/reuse;
- split works without overlap;
- coalesce restores larger free region;
- double-free handled according to debug contract;
- metrics internally consistent;
- deterministic fragmentation workload;
- two policies compared with same workload;
- sanitizer/debug invariant checks clean on supported host;
- README includes limitations + layout diagrams;
- transfer feature.
