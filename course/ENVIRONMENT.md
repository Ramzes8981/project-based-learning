# Course Environment

Canonical environment нужен для воспроизводимости Linux-specific labs, но setup не является отдельным учебным модулем.

## Desktop: Windows + WSL2 + Ubuntu

Для Windows основной path — WSL2/Ubuntu.

В PowerShell (администратор), если WSL ещё не установлен:

```powershell
wsl --install
```

Проверь версию:

```powershell
wsl -l -v
```

Новые установки через `wsl --install` по текущей Microsoft documentation используют WSL 2 по умолчанию. Дополнительная официальная инструкция остаётся optional reference:

- https://learn.microsoft.com/windows/wsl/install

После запуска Ubuntu:

```bash
sudo apt update
sudo apt install build-essential clang gdb git make python3 python3-pip \
    strace pkg-config
```

Некоторые поздние labs добавят packages just-in-time (`libfuse3-dev`, networking/debug tools и т.п.). Не устанавливай огромный toolset заранее.

## Где хранить code

Предпочтительно Linux filesystem внутри WSL:

```text
~/systems-course/
```

а не `/mnt/c/...`, особенно для labs с permissions, symlinks, Unix sockets и filesystem behavior.

## C profile

Baseline:

```bash
cc -std=c17 -Wall -Wextra -Wpedantic -g source.c -o program
```

Memory/debug profile:

```bash
cc -std=c17 -Wall -Wextra -Wpedantic -g \
  -fsanitize=address,undefined -fno-omit-frame-pointer \
  source.c -o program
```

Rule: **zero unexplained warnings**.

POSIX features вводятся deliberate feature-test macros only when needed, например:

```text
-D_POSIX_C_SOURCE=200809L
```

Linux-specific APIs (`ptrace`, namespaces, `/proc`) явно помечаются как Linux-specific.

## Rust

Rust Systems Bridge использует stable Rust через `rustup`.

Официально рекомендуемый WSL/Linux installer на текущем сайте Rust:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Optional reference:

- https://www.rust-lang.org/tools/install

После установки:

```bash
rustc --version
cargo --version
rustup component add rustfmt clippy
```

Основной workflow:

```text
cargo check
cargo fmt
cargo clippy
cargo test
```

Nightly/Miri/sanitizer-specific Rust tooling вводится только если конкретный lab действительно требует его.

## Python

Python 3 — вспомогательный язык курса для:

- test harness;
- fixtures;
- load generator;
- benchmark analysis;
- tooling, которое не является целью C/Rust урока.

Основной systems implementation не переносится на Python ради удобства.

## Android / метро

Phone — полноценное устройство для **теории курса**, потому что required Markdown находится в repo и написан mobile-first.

Можно использовать GitHub app/browser/offline clone/reader.

Termux optional для:

- tiny C/Rust-ish experiments where practical;
- shell commands;
- Git;
- небольших edits.

Не используй Android как canonical runtime для:

- namespaces/cgroup labs;
- FUSE;
- Linux ptrace debugger;
- platform-sensitive performance tests.

## macOS

Early C/Rust/algorithms/architecture work можно выполнять на macOS, но Linux-specific Modules 2+ должны проверяться в canonical Linux environment.

## Tools just in time

```text
compiler/Git        Module 0
ASan/UBSan/GDB      Module 1
Cargo/clippy        Module 1B
strace/termios      Module 2
objdump/readelf     Modules 3/8
mmap/perf tools     Module 4
Wireshark/socket    Module 5
/proc/unshare       Module 6
libfuse3            Module 7
ptrace/binutils     Module 8
load generator      Modules 5/9
```

## Project hygiene

Каждый milestone оставляет:

- source;
- tests;
- README/design notes;
- transfer feature;
- debugging story;
- small meaningful Git commits.

Не коммить generated binaries/huge benchmark artifacts без необходимости.
