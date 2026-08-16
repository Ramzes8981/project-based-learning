# 1B.4 — Почему reference не может пережить данные

**Теория:** ~70 мин · **Практика:** ~65 мин · **С телефона:** теория — да

← [`03-borrowing-references.md`](03-borrowing-references.md) · → [`05-option-result-errors.md`](05-option-result-errors.md)

## Проблема из C

Dangling pointer возникал, когда pointer жил дольше target object. Rust reference тоже не «магически бессмертен» — compiler должен доказать, что borrowed data живёт достаточно долго.

## Lifetime как relationship

**Время жизни (lifetime)** в Rust annotation описывает relationship между references, а не timer и не ручное продление object lifetime.

Плохая идея:

```rust
fn bad() -> &str {
    let s = String::from("temporary");
    &s
}
```

Такой reference пережил бы owner `s`; safe Rust rejects program.

## Slice

Slice — borrowed view на contiguous sequence:

```rust
&[T]
&mut [T]
&str
```

Он несёт pointer-like location + length contract, поэтому caller не должен отдельно угадывать array length как в C pointer API.

`&str` дополнительно гарантирует valid UTF-8 bytes.

## Lifetime elision

Во многих function signatures compiler выводит lifetime relationships автоматически:

```rust
fn first(xs: &[i32]) -> Option<&i32>
```

Explicit annotations нужны, когда relationship неоднозначен/важен для API, а не для украшения каждой reference.

## Практика

Напиши function, возвращающую slice-prefix входного slice при допустимой длине через `Option<&[T]>`. Затем объясни, почему result не может быть used после owner input data.

Разбор: [`04-lifetimes-slices.solution.md`](04-lifetimes-slices.solution.md).

## Exit check

Что lifetime annotation **не** делает с runtime lifetime object-а?