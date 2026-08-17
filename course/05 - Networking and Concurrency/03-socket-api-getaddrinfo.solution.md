# Разбор 5.3

A correct implementation should visibly separate ownership:

```text
addrinfo list: freeaddrinfo exactly once
candidate socket: close on failed connect/bind attempt
listening fd: stays open while accepting
accepted fd: close after that client is done
```

Do not return first `getaddrinfo` candidate assumption as universal truth. Iterate candidates until one succeeds or list exhausted.

For each length passed to allocation/serialization, validate arithmetic before multiplication/addition; socket API does not make buffer math safe automatically.