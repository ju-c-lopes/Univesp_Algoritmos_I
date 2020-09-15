"""

Problema Prático 5.2

Escreva uma função chamada potencias() que apanhe um inteiro positivo n como entrada e exiba,
na tela, todas as potências de 2, desde 2^1 até 2^n.

# >>> potencias(6)
  2 4 8 16 32 64

"""


def potencias(n):
    """
    Mostrará na tela o número 2 elevado a potência escolhida
    Exemplo: 2 ** 1, 2 ** 2, 2 ** 3 ... 2 ** n
    """
    for i in range(n):
        elevados = 2 ** (i + 1)
        print(elevados, ' ', end='')


