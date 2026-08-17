# Разбор 2.7

Для pipeline логично объединить children в process group:

```text
shell PG

foreground command PG
  ├─ A
  └─ B
```

Terminal foreground group получает interactive signals как группа, а shell остаётся отдельным управляющим process.

Core milestone может ограничиться более простой signal disposition моделью; если реализуешь process groups как transfer, нужно аккуратно продумать `setpgid`, terminal foreground control и races setup. Не добавляй их без тестового плана.
