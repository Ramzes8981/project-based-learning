# Разбор 5.2

Correct conclusion is independent of one experiment's chunk sizes:

```text
TCP preserves byte order, not application write boundaries.
```

Therefore receiver logic must tolerate:

- one frame split across many reads;
- several frames arriving in one read;
- EOF in the middle of an incomplete frame;
- short send/write on sender side.

UDP differs because one receive operation observes datagram boundaries (subject to buffer/truncation API behavior), but reliability/order remain separate concerns.