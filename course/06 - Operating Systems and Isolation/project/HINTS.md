# Isolation Lab — Hints

## Hint 1

Не начинай с C `clone` flags. Сначала докажи concept через `unshare` command.

## Hint 2

Сравни `/proc/self/ns/*` identifiers внутри и снаружи.

## Hint 3

PID namespace становится понятнее, если помнить: один task может иметь разные visible PIDs в nested namespaces.

## Hint 4

Если cgroup write запрещён, исследуй delegation/membership и document environment. Не меняй host policy вслепую.

## Hint 5

Каждый isolation claim дополни вопросом: «какой resource всё ещё shared?».
