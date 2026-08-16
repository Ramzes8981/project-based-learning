# Разбор упражнения 1C.3

Хорошее разделение для protocol parser:

```text
read_from_fd() -> raw bytes
parse_frame(bytes) -> structured request/error
execute(request, store) -> response
write_to_fd(response)
```

`parse_frame` можно тестировать на десятках fixtures без socket. System test затем отдельно проверяет реальный socket lifecycle.
