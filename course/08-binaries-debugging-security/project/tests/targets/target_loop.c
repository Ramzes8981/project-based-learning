#include <stdio.h>

__attribute__((noinline)) int marker(int x)
{
    return x * 2 + 1;
}

int main(void)
{
    int sum = 0;
    for (int i = 0; i < 3; ++i) {
        sum += marker(i);
    }
    printf("sum=%d\n", sum);
    return sum == 9 ? 0 : 1;
}
