"""

Elaborar um programa que leia duas matrizes do tipo vetor para o armazenamento de nomes de pessoas, s
endo a matriz A com 20 elementos e a matriz B com 30 elementos. Construir uma matriz C,
sendo esta a junção das matrizes A e B. Desta forma, a matriz C deve ter a capacidade de armazenar 50 elementos. A
presentar os elementos da matriz C.

"""

A = [0 for x in range(20)]
B = [0 for x in range(30)]
C = [0 for x in range(50)]

for i in range(0, 20):
    A[i] = input("Digite um nome: ")

for i in range(0, 30):
    B[i] = input("Digite um nome: ")

for i in range(0, 50):
    if i < 20:
        C[i] = A[i]
    else:
        C[i] = B[i - 20]

for i in range(0, 50):
    print("C[{}] = {}".format(i, C[i]))
