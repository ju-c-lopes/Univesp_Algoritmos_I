"""

Problema Prático 5.7

Escreva uma função xmult() que aceite duas listas de inteiros como entrada e retorne uma lista
contendo todos os produtos de inteiros da primeira lista com os inteiros da segunda lista.

# >>> xmult([2], [1, 5])
  [2, 10]
# >>> xmult([2, 3], [1, 5])
  [2, 10, 3, 15]
# >>> xmult([3, 4, 1], [2, 0])
  [6, 0, 8, 0, 2, 0]

"""


def xmult(l1, l2):
    """
    Multiplicará os valores da primeira lista com os da segunda lista, propriedade distributiva
    """
    lista = list()
    for i in l1:
        for j in l2:
            lista.append(i * j)
    return lista
