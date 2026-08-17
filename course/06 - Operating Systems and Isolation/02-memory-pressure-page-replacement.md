# 6.2 — Что делает ОС, когда активных страниц больше, чем физической памяти

**Теория:** ~80 мин · **Лаб:** ~75 мин · **С телефона:** теория — да

← [`01-scheduling-process-states.md`](01-scheduling-process-states.md) · → [`03-deadlocks-semaphores-condvars.md`](03-deadlocks-semaphores-condvars.md)

## Проблема

Virtual address spaces can collectively reference more memory than fits in RAM. OS must decide which page contents stay resident and which can be reclaimed/reloaded/swapped according to backing and policy.

## Resident vs mapped

A mapped virtual page does not imply its data is resident in physical RAM now. Some pages can be recreated from file, zero-filled, dropped when clean, or written to swap/backing according to system configuration.

## Page replacement intuition

Ideal “evict page that will not be needed soon” requires knowing future. Real kernels approximate locality using access/reference information and complex policies.

Do not memorize one textbook FIFO/LRU as literal Linux algorithm. Textbook policies are models for reasoning about locality and misses.

## Memory pressure

When reclaim cannot keep up, application can spend substantial time faulting/reloading pages; severe working-set mismatch may cause **thrashing**. System can invoke OOM policy if allocation cannot be satisfied under constraints.

## cgroup connection preview

Later cgroup can impose memory limit below machine RAM. Then “host has free memory” does not imply process group can allocate more.

## Lab safety

Never intentionally exhaust host RAM. Use modest controlled allocation, `/proc/<pid>/status`/`smaps` where permitted, and optional delegated cgroup limit in project environment.

## Exit check

Why can process have large virtual size, smaller RSS, and still later fault in more pages without a bug?