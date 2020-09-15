"""

Problema Prático 3.7

Escreva um laço for que exiba a seguinte sequência de números, um por linha.

a) Inteiros de 3 até 12, inclusive este.
b) Inteiros de 0 até (mas não incluindo) 9, com um passo de 2 em vez do padrão 1 (isto é, 0, 2, 4, 6, 8).
c) Inteiros de 0 até (mas não incluindo) 24, com um passo de 3.
d) Inteiros de 3 até (mas não incluindo) 12, com passo 5

"""

# Exercicio a)

for x in range(3, 13):
    print(x)

print('\n')

# Exercicio b)

for a in range(0, 10, 2):
    print(a)

print('\n')

# Exercicio c)

for i in range(0, 24, 3):
    print(i)

print('\n')

# Exercicio d)

for t in range(3, 12, 5):
    print(t)
