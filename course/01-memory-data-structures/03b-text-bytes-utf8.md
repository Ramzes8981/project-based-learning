# 1.3B — Почему текст и bytes — не одно и то же

**Теория:** ~55 мин  
**Практика:** ~40 мин  
**С телефона:** да; hex-практика — ПК

← [`03-const-types-bits.md`](03-const-types-bits.md) · → [`04-lifetime-ownership.md`](04-lifetime-ownership.md)

## Проблема

В C string мы видели `char[]` и конечный `\0`. Легко сделать неверный вывод:

> один `char` = один видимый символ.

Для ASCII-примера это часто выглядит правдой. Для реального Unicode text — нет.

## Bytes сначала

**Byte** — минимальная адресуемая единица памяти C; `sizeof(char) == 1` по определению языка. Byte не обязан сам по себе быть «буквой».

Файл и сеть тоже в конечном счёте передают sequences of bytes. Значение этих bytes задаёт формат/encoding.

## Unicode: символам нужны номера

Unicode задаёт множество **code points** — абстрактных идентификаторов символов/знаков, например `U+0041` для `A`.

Но code point ещё нужно превратить в bytes.

## UTF-8

**UTF-8** — encoding Unicode code points в последовательности из 1–4 bytes.

ASCII characters занимают один byte и сохраняют привычные значения. Многие другие characters занимают несколько bytes.

```text
"A"   -> 1 UTF-8 byte
"Ж"   -> 2 UTF-8 bytes
"€"   -> 3 UTF-8 bytes
```

Поэтому:

```text
byte length != number of Unicode code points
```

а «количество видимых символов для пользователя» ещё сложнее из-за combining marks/grapheme clusters. Core курса не строит Unicode UI library; важно не путать уровни.

## C string добавляет ещё один контракт

Если UTF-8 bytes хранятся как C string:

```text
UTF-8 encoded bytes ... '\0'
```

`strlen` возвращает число bytes до `\0`, **не число Unicode characters**.

## Binary data может содержать zero byte

Произвольный binary payload способен содержать `0` внутри. Поэтому C string functions нельзя использовать как универсальные byte-buffer functions.

Для binary data честный API обычно несёт отдельную длину:

```c
void consume(const unsigned char *data, size_t len);
```

## Неправильная mental model

> «Если bytes печатаются как текст, значит это текст».

Нет. Нужен encoding contract. Одна и та же последовательность bytes без договорённости не обязана иметь один и тот же textual meaning.

## Практика

Создай UTF-8 source file со строками `A`, `Ж`, `€`. Для каждой:

1. выведи `strlen`;
2. выведи каждый byte как hex;
3. заранее предскажи, сколько bytes увидишь;
4. объясни, почему `strlen("Ж")` не отвечает на вопрос «сколько здесь букв?».

## Causal questions

1. Почему network protocol, который разрешает arbitrary bytes, не может искать конец payload через `\0`?
2. Почему `strlen` корректно называет длину C string в bytes и одновременно не считает Unicode characters?
3. Что должно быть частью API, если функция получает binary data?

## Exit check

Ты различаешь byte sequence, C string, Unicode code point и UTF-8 encoding.