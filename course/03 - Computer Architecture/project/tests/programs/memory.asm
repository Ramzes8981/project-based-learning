; Store 55 at memory address 10 and load it into R2
LOADI R0, 10
LOADI R1, 55
STORE R1, [R0]
LOAD R2, [R0]
HALT
