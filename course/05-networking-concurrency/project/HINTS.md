# Concurrent KV Server — Hints

## 1. Prove framing before threads

Feed parser arbitrary chunk boundaries in memory first. Networking should not be required to reproduce codec bug.

## 2. Separate connection state from shared store

Per-connection frame buffers are usually owned by one handler/event state. Shared KV/metrics need explicit synchronization.

## 3. Define fd ownership transfer

Before enqueue:

```text
acceptor owns client fd
```

After successful enqueue:

```text
queue/worker owns client fd
```

On enqueue failure owner does not magically change.

## 4. Condition variable waits on predicate

Always `while (!predicate) wait`, with predicate protected by same mutex.

## 5. Never optimize lock granularity first

Start with smallest design you can prove correct, measure contention, then split locks with new invariants/tests.

## 6. Tail latency

If p99 grows while service work stays flat, record queue-wait separately before blaming socket/TCP.

## 7. Load tool

Bundled `loadgen.py` is closed-loop. Use it for controlled comparisons, not unsupported “maximum RPS” claims.