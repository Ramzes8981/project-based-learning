# Разбор 1.4

A. **Допустимо**, если caller object действительно остаётся жив и pointer остаётся в его bounds.

B. **Недопустимо после return**: lifetime local automatic object закончился; pointer становится dangling.

C. **Допустимо при заявленных условиях**: array object жив, storage не заменён, pointer относится к существующему element.

D. **Допустимо**, если helper не сохраняет pointer дольше call и исходный object жив весь call. `const` ограничивает mutation через этот access path, но не управляет lifetime.

E. **Недопустимо после окончания lifetime local object**. Более долгоживущая pointer variable не продлевает target lifetime.

Это решение намеренно соответствует всем пяти сценариям A–E из урока.