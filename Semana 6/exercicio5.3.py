"""

Problema Prático 5.3

Escreva a função aritmética(), que aceita uma lista de inteiros como entrada e retorna
True se eles formarem uma sequência aritmética. (Uma sequência de inteiros é uma sequência
aritmética se a diferença entre os itens consecutivos da lista for sempre a mesma.)

# >>> aritmética([3, 6, 9, 12, 15])
  True
# >>> aritmética([3, 6, 9, 11, 14])
  False
# >>> aritmética([3])
  True

"""


def aritmetica(lista):
    """
    Verifica a sequência numérica dos elementos da lista
    """
    for i in range(0, len(lista) - 1):
        dif = lista[1] - lista[0]
        dif_now = lista[i + 1] - lista[i]
        if dif_now == dif:
            ver = True
        else:
            ver = False
        if not ver:
            return False
    return True
