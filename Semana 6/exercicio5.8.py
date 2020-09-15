"""

Problema Prático 5.8

Uma forma de classificar uma lista de n números diferentes em ordem crescente é
executar n-1 passadas sobre os números na lista. Cada passada compara todos os
números adjacentes na lista e os inverte, se estiverem fora de ordem. Ao final
da primeira passada, o maior item estará no final da lista (no índice n-1).
Portanto, a segunda passada pode parar antes de alcançar o último elemento, pois
ele já está na posição correta; a segunda passada colocará o segundo maior item
na penúltima posição. Em geral, a passada n-1, a lista estará em ordem crescente.

Escreva uma função bubbleSort() que aceite uma lista de números como entrada e
classifique a lista usando essa técnica.

# >>> lst = [3, 1, 7, 4, 9, 2, 5]
# >>> bubblesort(lst)
# >>> lst
  [1, 2, 3, 4, 5, 7, 9]

"""


def bubblesort(lista):
    """
    Ordenará a lista informada em ordem crescente
    """
    it = len(lista)
    for i in range(it - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
