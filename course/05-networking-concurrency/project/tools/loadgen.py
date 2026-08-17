#!/usr/bin/env python3
"""Closed-loop concurrency driver for the course KV protocol.

Each worker sends one request and waits for its response before issuing the next
request. This is useful for repeatable concurrency/regression comparisons, but
it is NOT an open-loop arrival generator and must not be used alone to claim a
maximum sustainable external arrival rate. Server slowdown reduces offered
load automatically.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import statistics
import time
from dataclasses import dataclass

from client import KVClient


@dataclass(frozen=True)
class Sample:
    latency_ms: float
    ok: bool


def percentile(values: list[float], p: float) -> float:
    if not values:
        raise ValueError("percentile requires at least one value")
    if not 0.0 <= p <= 100.0:
        raise ValueError("percentile must be in [0, 100]")
    ordered = sorted(values)
    rank = (len(ordered) - 1) * (p / 100.0)
    lo = int(rank)
    hi = min(lo + 1, len(ordered) - 1)
    fraction = rank - lo
    return ordered[lo] * (1.0 - fraction) + ordered[hi] * fraction


def one_request(host: str, port: int, index: int) -> Sample:
    started = time.perf_counter()
    ok = False
    try:
        with KVClient(host, port) as client:
            key = f"k{index}".encode()
            value = f"v{index}".encode()
            client.set(key, value)
            got = client.get(key)
            ok = got == value
    except (OSError, ValueError, RuntimeError):
        ok = False
    elapsed_ms = (time.perf_counter() - started) * 1000.0
    return Sample(elapsed_ms, ok)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Closed-loop KV concurrency driver. Each worker waits for its response; "
            "results do not by themselves establish open-loop overload capacity."
        )
    )
    parser.add_argument("host")
    parser.add_argument("port", type=int)
    parser.add_argument("--requests", type=int, default=100)
    parser.add_argument("--concurrency", type=int, default=8)
    args = parser.parse_args()

    if args.requests <= 0:
        raise SystemExit("--requests must be > 0")
    if args.concurrency <= 0:
        raise SystemExit("--concurrency must be > 0")

    started = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        samples = list(
            pool.map(
                lambda i: one_request(args.host, args.port, i),
                range(args.requests),
            )
        )
    elapsed = time.perf_counter() - started

    latencies = [sample.latency_ms for sample in samples]
    successes = sum(sample.ok for sample in samples)
    failures = len(samples) - successes

    print("model=closed-loop")
    print(f"requests={len(samples)} successes={successes} failures={failures}")
    print(f"elapsed_s={elapsed:.3f}")
    print(f"completed_rps={len(samples) / elapsed:.2f}")
    print(f"latency_mean_ms={statistics.fmean(latencies):.3f}")
    print(f"latency_p50_ms={percentile(latencies, 50):.3f}")
    print(f"latency_p95_ms={percentile(latencies, 95):.3f}")
    print(f"latency_p99_ms={percentile(latencies, 99):.3f}")


if __name__ == "__main__":
    main()
