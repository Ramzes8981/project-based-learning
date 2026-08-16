# Разбор 1C.3

Один минимальный pattern:

```c
typedef struct {
    size_t calls;
    size_t fail_on;
} FailPlan;

void *test_alloc(size_t bytes, void *ctx)
{
    FailPlan *plan = ctx;
    plan->calls += 1;
    if (plan->calls == plan->fail_on) {
        return NULL;
    }
    return malloc(bytes);
}
```

Production code не обязан принимать этот exact signature. Важна design idea: failure boundary controllable and deterministic.

Test oracle после forced failure должен проверить **state preservation**, а не только returned status.

Unix-specific `ssize_t`, file descriptors, short I/O and socket examples intentionally removed from this early module; those concepts are introduced later.