#include <stdio.h>

__attribute__((noinline)) static int level3(int x) { return x + 3; }
__attribute__((noinline)) static int level2(int x) { return level3(x) + 2; }
__attribute__((noinline)) static int level1(int x) { return level2(x) + 1; }

int main(void)
{
    int value = level1(10);
    printf("value=%d\n", value);
    return value == 16 ? 0 : 1;
}
