#include <stdatomic.h>

int main(void)
{
    atomic_int counter = ATOMIC_VAR_INIT(0);
    (void)atomic_fetch_add(&counter, 1);
    return atomic_load(&counter) == 1 ? 0 : 1;
}
