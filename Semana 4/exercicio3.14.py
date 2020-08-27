"""

Problema Prático 3.14

Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista.
Você pode considerar que a lista não estará vazia. A função não deverá retornar nada.

# >>> ingredientes = ['farinha', 'açucar', 'manteiga', 'maçãs']
# >>> trocaPU(ingredientes)
# >>> ingredientes
  ['maçãs', 'açucar', 'manteiga', 'farinha']

"""


def trocapu(lst):
    """ Troca o primeiro e o último elemento da lista """
    lst[0], lst[-1] = lst[-1], lst[0]
