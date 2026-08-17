#include <stdio.h>

volatile long course_global = -1;

int marker(int x)
{
    return x + 1;
}

int main(void)
{
    int value = marker(41);
    printf("value=%d global=%ld\n", value, course_global);
    return value == 42 ? 0 : 1;
}
