"""

Construir um programa que apresente a soma dos cem primeiros números naturais (1 + 2 + 3 +...+ 98 + 99 + 100).

"""

N = 1
soma = 0

while N <= 100:
    soma = soma + N
    N += 1

ex = """N = 1
soma = 0

while N <= 100:
    soma = soma + N
    N += 1\n"""

print(ex, "\nA soma dos primeiros cem números naturais é ", soma)
