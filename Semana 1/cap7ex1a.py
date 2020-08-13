"""

Elaborar um programa que leia 12 elementos numéricos inteiros em uma matriz do tipo vetor.
Coloque-os em ordem decrescente e apresente os elementos ordenados.

"""

n = [0 for x in range(12)]

for i in range(0, 12):
    n[i] = i + 1

for i in range(0, 11):
    for j in range(i + 1, 12):
        if n[i] < n[j]:
            x = n[i]
            n[i] = n[j]
            n[j] = x

for i in range(0, 12):
    print(n[i])
