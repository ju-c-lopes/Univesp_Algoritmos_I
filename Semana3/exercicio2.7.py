"""

Problema Prático 2.7

Dada a lista de notas de trabalho de casa dos alunos

#    >>> notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

escreva:

a) Uma expressão que avalia para o número de 7 notas.

b) Uma instrução que muda a última nota para 4.

c) Uma expressão que avalia a nota mais alta.

d) Uma instrução que classifica as notas da lista.

e) Uma expressão que avalia para a média das notas.

"""

# Letra a)

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print('Exercicio a)\nnotas.count(7) = ', notas.count(7))
print('\n')

# Letra b)

notas[-1] = 4

print('Exercicio b)\nnotas[9] = 4')
print(notas[-1])
print('\n')

# Letra c)

print('Exercicio c)\nmax(notas) = ', max(notas))
print('\n')

# Letra d)

print('Exercicio d)\nnotas.sort() = ', end="")
notas.sort()
print(notas)
print('\n')

# Letra e)

print('Exercicio e)\nsum(notas) / len(notas) = ', sum(notas) / len(notas))