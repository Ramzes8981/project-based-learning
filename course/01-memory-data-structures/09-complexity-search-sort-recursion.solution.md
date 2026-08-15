# Разбор 1.9

Для half-open interval `[lo, hi)`:

```text
lo = 0
hi = n
while lo < hi:
    mid = lo + (hi-lo)/2
    if a[mid] < target:
        lo = mid + 1
    else:
        hi = mid
```

После цикла `lo` — lower-bound position; затем отдельно проверяется, равен ли `a[lo]` target и находится ли `lo < n`.

Этот вариант показывает важную идею: algorithm и contract результата нужно проектировать вместе.

Сумма `0+1+...+(n-1) = n(n-1)/2` имеет ведущий член порядка `n^2`, поэтому `Θ(n^2)`.
