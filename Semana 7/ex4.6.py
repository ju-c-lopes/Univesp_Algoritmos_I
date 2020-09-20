from random import randint

lin = int(input('Qtde de linhas = '))
col = int(input('Qtde de colunas = '))

m = []
i = 0

while i < lin:
    m.append([])
    j = 0
    while j < col:
        m[i].append(randint(0, 20))
        j += 1
    i += 1

print('\nEsta é a lista M gerada')
print('M =', m)

print('\nExibindo como matriz fica assim')
i = 0

while i < lin:
    j = 0
    print('|', end='')
    while j < col:
        print(end=''"{0:4} ".format(m[i][j], end=''))
        j += 1
    print(' |')
    i += 1
