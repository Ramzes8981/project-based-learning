# Module 5 — Networking and Concurrency

**Status:** CORE  
**Estimated effort:** 55–70 hours (~8–10 weeks)  
**Core milestone:** concurrent TCP key/value server

## Prerequisites

- robust file-descriptor I/O from Module 2;
- hash table from Module 1;
- basic performance measurement from Module 4;
- pointers, dynamic memory and structs.

No prior networking or threading knowledge is assumed.

## Sources

- **PRIMARY THEORY (RU):** Stepik — Основы компьютерных сетей.
- **PROGRAMMING PRIMARY:** Beej's Guide to Network Programming: https://beej.us/guide/bgnet/
- **REFERENCE:** current man pages / POSIX socket APIs; Wireshark documentation.
- **CONCURRENCY PRIMARY:** Dive into Systems parallelism/concurrency sections + selected OSTEP concurrency chapters.

Do not study two full networking courses in parallel. Stepik explains the network; Beej is used when code needs sockets.

---

# Outcomes

The learner can:

- explain Ethernet → ARP → IP → TCP/UDP → socket/application data;
- reason about subnet/routing basics;
- write address-family-independent client/server code using `getaddrinfo()`;
- treat TCP as a byte stream, not as a message protocol;
- implement framing and robust partial send/receive loops;
- explain blocking, threads and event-driven I/O;
- protect shared state with mutexes and reason about races/deadlocks;
- implement a bounded concurrent server;
- measure latency/throughput/errors/saturation under load.

---

# Unit 5.1 — Layered network model

### Learn

- frame / packet / segment / application message;
- MAC address;
- ARP;
- IPv4 address and subnet prefix;
- router/default gateway;
- ICMP;
- ports;
- UDP vs TCP.

Use OSI vocabulary only where it helps communication; understand the concrete TCP/IP stack rather than memorizing seven layers for a quiz.

### Lab

Capture a small exchange with Wireshark and identify:

- Ethernet addresses;
- IP endpoints;
- transport protocol/ports;
- application bytes.

### Situational question

Two hosts share an IP subnet but cannot communicate after one host's subnet mask is changed. Explain what decision each host makes before it ever sends to a gateway.

---

# Unit 5.2 — TCP behavior

### Learn

- connection establishment;
- ordered reliable byte stream;
- sequence/acknowledgement intuition;
- retransmission/flow-control concept;
- connection close;
- TCP does **not** preserve application message boundaries.

### Required misconception check

If a client calls `send()` once with 100 bytes, the server is **not** guaranteed to receive exactly one 100-byte `recv()` result.

### Lab

Observe a small TCP connection with Wireshark and map code-level actions to packets/segments.

---

# Unit 5.3 — Socket API

### Learn

- `socket`;
- `bind`;
- `listen`;
- `accept`;
- `connect`;
- `send`/`recv` or `read`/`write`;
- `getaddrinfo`;
- network byte order;
- `SO_REUSEADDR` concept;
- connection and descriptor cleanup.

### Project slice

Build a TCP echo server/client.

### Self-check

- works for multiple sequential connections;
- handles peer disconnect;
- reports bind/connect errors;
- does not assume a single send/recv transfers all bytes.

---

# Unit 5.4 — Application protocol and framing

### Learn

A real application protocol needs explicit framing.

Choose one course protocol, e.g. length-prefixed frames:

```text
[4-byte length][payload bytes]
```

Define:

- byte order;
- maximum frame size;
- invalid-length behavior;
- request/response types;
- encoding assumptions.

### Project slice

Turn the echo server into a tiny KV protocol using the Module 1 hash table:

- `SET key value` or equivalent encoded request;
- `GET key`;
- explicit success/error response.

### Security/reliability edge cases

- declared length larger than allowed;
- peer disconnects mid-frame;
- zero-length frame;
- integer overflow while allocating payload buffer.

---

# Unit 5.5 — Threads and shared state

### Learn

- process vs thread;
- shared address space;
- race condition;
- critical section;
- mutex;
- condition variable;
- deadlock conditions at a practical level;
- bounded queue concept.

### Lab

Create a deterministic counter/race demonstration, then fix it with synchronization.

### Situational questions

- Why can `counter++` race even though it is one source-code expression?
- What happens if a mutex is held while performing slow blocking network I/O?
- Why can an unbounded request queue turn overload into memory exhaustion?

---

# Unit 5.6 — Thread-pool server

### Project slice

Implement:

```text
acceptor -> bounded work queue -> N worker threads -> shared KV store
```

Required behavior:

- fixed configurable worker count;
- bounded queue;
- synchronized store access;
- clean connection close;
- graceful shutdown plan.

### Backpressure

Define what happens when the queue is full. A bounded system must make an explicit choice: block, reject or shed work.

---

# Unit 5.7 — Non-blocking/event-driven model

### Learn

- blocking vs non-blocking descriptors;
- readiness;
- `poll()` as the core teaching API;
- event loop;
- per-connection state machine;
- why partial read/write handling becomes stateful.

`epoll` can be introduced as Linux-specific Stretch after `poll()` is understood.

### Guided lab

Build or study a small `poll()`-based server and compare the control flow with the thread-pool version.

The core milestone does not require two production-quality implementations; the learner must, however, be able to explain the trade-off.

---

# CS checkpoint — Graphs and priority queues

Algorithms must not disappear from the course after Module 1.

### Learn

- graph representation: adjacency list/matrix;
- BFS;
- DFS;
- weighted graph concept;
- priority queue/heap review;
- Dijkstra under non-negative edge weights;
- complexity intuition.

### Applied exercise

Model a small network topology and compute reachability / shortest path. This is an algorithms exercise connected to networking, not a routing-protocol implementation.

### What goes wrong if…?

- Dijkstra is used with negative-weight edges?
- BFS is used as a shortest-path algorithm on differently weighted edges?

---

# Unit 5.8 — Load testing and service metrics

### Learn

- throughput (requests/s);
- latency distribution, not only average;
- p50/p95/p99 intuition;
- error rate;
- saturation signal;
- open connections / queue depth.

### Project instrumentation

Measure at least:

- total requests;
- successful/failed requests;
- request latency;
- queue depth or rejected work;
- connections.

Use a simple Python load generator if useful; the purpose is the server, not reimplementing a load-test framework in C.

---

# Core milestone rubric — Concurrent KV Server

### Correctness

- framed protocol;
- `GET`/`SET`-like operations;
- robust partial I/O;
- multiple clients;
- bounded concurrency;
- graceful handling of malformed/oversized requests.

### Concurrency

- no known data races in intended shared state;
- synchronization policy documented;
- queue has a bound/backpressure policy;
- shutdown path does not abandon locks/threads silently.

### Performance evidence

Provide a reproducible small benchmark with throughput and latency percentiles. No arbitrary "fast" claim.

### Transfer task

Choose one:

- timeouts;
- connection limits;
- `poll()` implementation;
- read/write operation metrics;
- read-write lock experiment;
- protocol versioning field.

### Engineering review

Compare thread-per-connection, thread pool and event loop for complexity, memory, failure modes and expected workload.

---

# Exit gate

Given a slow/overloaded concurrent server, the learner can separate network framing bugs, race conditions, queue saturation and CPU/memory bottlenecks instead of treating all of them as "the server is slow".