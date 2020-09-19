"""

Problema Prático 4.4

Escreva a função par() que toma um inteiro positivo n como entrada e exibe na tela
todos os números entre 2 (inclusive) e n, que sejam divisíveis por 2 ou por 3, usando
este formato de saída:

# >>> even(17)
  2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16,

"""


def even(n):

    for i in range(2, n + 1):
        if i % 2 == 0 or i % 3 == 0:
            print(i, end=', ')
