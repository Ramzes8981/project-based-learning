# Разбор упражнения 1B.9

Каждый worker владеет своим `Arc` clone. Все clones ссылаются на один allocation с `Mutex<i64>`. Allocation освобождается после Drop последнего `Arc`.

`Mutex` сериализует critical section над `i64`; `Arc` лишь обеспечивает thread-safe shared ownership. Не держи guard дольше необходимого и не выполняй под ним ненужную blocking работу.
