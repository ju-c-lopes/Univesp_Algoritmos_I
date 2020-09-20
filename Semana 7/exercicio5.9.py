"""

Problema Prático 5.9

Escreva uma função soma2D() que aceita duas listas bidimensionais do mesmo tamanho
(ou seja, o mesmo número de linhas e colunas) como argumentos de entrada e incrementa
cada entrada da primeira lista com o valor da entrada correspondente da segunda lista

# >>> t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
# >>> s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
# >>> soma2D(t, s)
# >>> for linha in t:
          print(linha)

  [4, 8, 4, 5]
  [5, 2, 10, 3]
  [8, 4, 6, 6]

"""
from typing import List, Any

tam_linha = eval(input('\nQuantas linhas e quantas colunas deseja digitar?\nLinhas: '))
tam_coluna = eval(input('Colunas: '))

print('Digite os valores da primeira matriz: ')

matriz1 = list()
for i in range(tam_linha):
    col = list()
    for j in range(tam_coluna):
        print(f'[{i}][{j}]: ', end=' ')
        col.append(eval(input()))
    matriz1.append(col)


print('\nDigite os valores da segunda matriz: ')

matriz2 = list()
for i in range(tam_linha):
    col = list()
    for j in range(tam_coluna):
        print(f'[{i}][{j}]: ', end=' ')
        col.append(eval(input()))
    matriz2.append(col)


def soma2d(s, t):
    soma = list()
    for m in range(0, len(s)):
        colums = list()
        for n in range(0, len(t) + 1):
            som_col = s[m][n] + t[m][n]
            colums.append(som_col)
        soma.append(colums)
    return soma


print('\n')
soma = soma2d(matriz1, matriz2)
for i in soma:
    print(i)
