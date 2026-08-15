# 2.4 — Shell REPL и ограниченный parser

**Теория:** ~50 мин  
**Project slice:** ~3–5 часов  
**С телефона:** теория — да

← [`03-fork-exec-wait.md`](03-fork-exec-wait.md) · → [`05-redirection-dup2.md`](05-redirection-dup2.md)

## Цель

Построить command loop и deliberately limited grammar вместо иллюзии «split строку по пробелам = shell parser».

## REPL

Shell core loop:

```text
Read command line
Evaluate/parse
Execute
Print/return to prompt
Loop
```

Interactive shell также должен переживать errors одного command без завершения всего process.

## Course grammar v0

Поддерживаем:

```text
command arg1 arg2 ...
```

Whitespace разделяет tokens.

Пока **не поддерживаем**:

- quotes;
- escapes;
- variable expansion;
- globbing;
- command substitution;
- operators кроме тех, что появятся отдельно (`<`, `>`, `|`).

Это честный contract, а не «плохая реализация bash».

## Tokenization

Parser должен различать:

- empty line;
- whitespace-only;
- token count limit или dynamic argv;
- operator tokens позже.

Если используешь in-place tokenization, знай ownership: tokens могут быть pointers внутрь line buffer. Они валидны только пока жив buffer.

Это отличный practical lifetime example.

## Builtins

`cd` должен исполняться **в shell process**, иначе child изменит только свою working directory и сразу завершится.

То же относится к `exit` и многим shell-state builtins.

Разделение:

```text
builtin? -> execute in shell
external? -> fork/exec/wait
```

## Working directory

Current working directory — process attribute. Child обычно наследует её при fork; `chdir` shell process влияет на последующие commands.

## Project slice

Реализуй v0:

- prompt;
- read line;
- tokenize whitespace grammar;
- empty line;
- `cd`;
- `exit`;
- external argv execution;
- errors не убивают shell.

## Tests

Сценарии:

```text
(empty)
pwd
cd /tmp
pwd
/bin/echo one two
nonexistent_command
```

## Causal questions

1. Почему `cd` в forked child не меняет cwd parent shell?
2. Почему tokens pointing into line buffer не могут жить после освобождения buffer?
3. Почему quotes нельзя «случайно почти поддержать»?
4. Где проходит boundary parser vs executor?

## Подсказки

В проекте см. `HINTS.md`; готового parser code курс не даёт.

## Exit check

README проекта должен явно перечислять grammar v0 и unsupported syntax.
