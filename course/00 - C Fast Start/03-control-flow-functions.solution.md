# Разбор 0.3

```c
#include <stdio.h>

int clamp_score(int score)
{
    if (score < 0) {
        return 0;
    }
    if (score > 100) {
        return 100;
    }
    return score;
}

int main(void)
{
    int cases[] = {-1, 0, 50, 100, 101};
    for (int i = 0; i < 5; ++i) {
        printf("%d -> %d\n", cases[i], clamp_score(cases[i]));
    }
    return 0;
}
```

Ключевая идея — границы `0` и `100` принадлежат допустимому диапазону, поэтому проверяются случаи непосредственно рядом с ними.