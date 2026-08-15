# Разбор 2.2

Минимальная архитектура:

```text
main
 ├─ tcgetattr(stdin, &original)
 ├─ modified = original
 ├─ clear/set selected flags
 ├─ tcsetattr(... modified)
 ├─ read loop
 └─ tcsetattr(... original) on normal exit
```

Нужны проверки return values каждого terminal call.

Если используешь helper `enable_raw`, не прячь original settings в случайной static global без понимания lifetime. На этом этапе допустим небольшой explicit state struct/context.

Полная flag combination не приводится как solution: она должна следовать scope lab и текущей platform documentation, а не копироваться магической строкой.
