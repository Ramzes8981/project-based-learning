#!/usr/bin/env python3
"""Small deterministic load generator for the course KV server.

Not a production benchmark. It provides repeatable concurrency and latency samples.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import socket
import statistics
import time

from client import frame, read_response


def one(host: str, port: int, i: int) -> float:
    key = f"k{i % 100}".encode()
    value = f"v{i}".encode()
    start = time.perf_counter_ns()
    with socket.create_connection((host, port), timeout=3) as s:
        s.sendall(frame(0x02, key, value))
        status, _ = read_response(s, 0x02)
        if status != 0:
            raise RuntimeError(f"SET status {status}")
    return (time.perf_counter_ns() - start) / 1_000_000


def percentile(sorted_values: list[float], p: float) -> float:
    if not sorted_values:
        raise ValueError("no samples")
    index = int(round((len(sorted_values) - 1) * p))
    return sorted_values[index]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("host")
    ap.add_argument("port", type=int)
    ap.add_argument("--requests", type=int, default=1000)
    ap.add_argument("--concurrency", type=int, default=20)
    args = ap.parse_args()

    wall_start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as ex:
        latencies = list(ex.map(lambda i: one(args.host, args.port, i), range(args.requests)))
    elapsed = time.perf_counter() - wall_start
    ordered = sorted(latencies)

    print(f"requests={len(ordered)} elapsed_s={elapsed:.3f} throughput_rps={len(ordered)/elapsed:.1f}")
    print(f"mean_ms={statistics.fmean(ordered):.3f}")
    print(f"p50_ms={percentile(ordered, 0.50):.3f}")
    print(f"p95_ms={percentile(ordered, 0.95):.3f}")
    print(f"p99_ms={percentile(ordered, 0.99):.3f}")


if __name__ == "__main__":
    main()
