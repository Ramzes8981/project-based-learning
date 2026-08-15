# Разбор 5.3

Server resource sequence:

```text
getaddrinfo -> candidates
for candidate:
  socket
  bind
  if fail close
selected listening fd
listen
loop:
  accept -> client fd
  echo using robust recv/send
  close client fd
close listen fd on shutdown
freeaddrinfo when no longer needed
```

Ключевой skill — cleanup при каждой частичной failure, а не запоминание exact boilerplate.
