"""

Problema Prático 5.6

Escreva a função divisores(), que aceita um inteiro positivo n como entrada e retorna a lista de todos
os divisores positivos de n.

# >>> divisores(1)
  [1]
# >>> divisores(6)
  [1, 2, 3, 6]
# >>> divisores(11)
  [1, 11]

"""


def divisores(n):
    """
    Verifica quais são os divisores do número informado
    """
    div = list()
    for i in range(1, n + 1):
        if n % i == 0:
            div.append(i)
    return div
