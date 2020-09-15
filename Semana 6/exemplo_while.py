##


def nfat(L):
    n = 0
    fat = 1
    while fat <= L:
        n += 1
        fat *= n
    return n-1


print(nfat(20))

##

num = eval(input('Digite um número positivo: '))
while num < 0:
    num = eval(input('Digite um número positivo: '))

##

l = []

nome = input('Digite um nome: ')
while nome != '':
    l.append(nome)
    nome = input('Digite um nome: ')

for i in l:
    print(i)
