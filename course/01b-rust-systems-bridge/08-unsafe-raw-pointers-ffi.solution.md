# Разбор упражнения 1B.8

Минимальный raw-pointer блок безопасен только пока source object жив и не нарушены aliasing/alignment rules.

Для FFI основная мысль не в строке `unsafe`: Rust compiler **доверяет твоему extern declaration**. Если C symbol имеет другую signature/layout, unsafe obligation нарушен ещё до meaningful business logic.

Для `add_two` ограничивай test inputs так, чтобы C `int` addition не overflow: FFI не отменяет C undefined behavior.
