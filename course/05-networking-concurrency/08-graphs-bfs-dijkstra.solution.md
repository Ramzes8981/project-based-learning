# Разбор 5.8

BFS treats every edge as одинаковую unit cost. Поэтому minimum layers = minimum edge count.

Weighted graph требует учитывать разные costs. Dijkstra делает это через tentative distances + priority queue, но полагается на non-negative weights: когда smallest tentative vertex окончательно выбран, позднее negative edge не должна внезапно сделать его путь короче.
