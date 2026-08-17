; JZ must skip the first LOADI R1 when R0 == 0
LOADI R0, 0
JZ R0, target
LOADI R1, 1
target:
LOADI R1, 7
HALT
