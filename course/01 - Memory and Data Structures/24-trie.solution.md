# Разбор упражнения Optional 1C

При fixed children array из 26 pointers node содержит 26 pointer slots независимо от фактического branching. На 64-bit platform это уже примерно 208 bytes только под pointers до padding/flags — хороший пример memory trade-off.

Terminal marker обязателен: node для `r` в `car` может иметь child `t` для `cart`, поэтому «leaf == complete word» неверно.
