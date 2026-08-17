# Rust MiniKV — Acceptance

- `cargo fmt --check` clean;
- `cargo clippy` без необъяснённых warnings;
- `cargo test` проходит;
- set/get/update работают;
- missing key -> `None`;
- invalid constrained input -> typed `Err`;
- read methods не требуют `&mut self`;
- lookup не клонирует value без необходимости;
- нет unjustified `unsafe`;
- transfer feature + tests;
- README содержит C vs Rust comparison.

## Review-only

Преподаватель может попросить изменить API так, чтобы временно возник borrow conflict, и объяснить, почему compiler его запрещает и как redesign ownership решает задачу без бессмысленного clone.
