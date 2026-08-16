# Разбор упражнения 1.13

Главные invariants:

- каждая node принадлежит tree ровно один раз;
- ordering выполняется рекурсивно для каждой subtree;
- destroy в postorder освобождает children до parent и не использует node после `free`.

Если вставить строго возрастающие keys в обычный BST без balancing, каждый новый key уйдёт вправо: height станет порядка `n`, поэтому search деградирует до linear.
