# Modern Linux Isolation Lab

This is an **observation-first, disposable-environment lab**, not a mini-container platform.

## Safety order

1. Complete [`ENVIRONMENT_CHECKLIST.md`](ENVIRONMENT_CHECKLIST.md).
2. Record baseline `/proc`, namespace, cgroup and capability evidence.
3. Prefer unprivileged/user/delegated mechanisms.
4. If write permission/delegation absent, stay read-only and document limitation.
5. Never run broad cleanup/kill/mount/cgroup commands against host production state.

## Milestones

- scheduling/memory observation;
- process/IPC inspection;
- namespace view changes;
- cgroup resource bound in safe subtree;
- capability observation/restriction where supported;
- final threat-model note: what remains unisolated.

Docs: [`SPEC.md`](SPEC.md) · [`ACCEPTANCE.md`](ACCEPTANCE.md) · [`TESTS.md`](TESTS.md) · [`HINTS.md`](HINTS.md).