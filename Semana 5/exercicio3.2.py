"""

Problema Prático 3.2

Traduza estas instruções condicionais em instruções if do Python:

a) Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'.

b) Se o nome está na lista ['Musial', 'Aaraon', 'Williams', Gehrig', 'Ruth'], exiba 'Um dos 5 maiores jogadores
de beisebol de todos os tempos!'.

c) Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto...'.

d) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.

"""
##

# Exercicio a)

idade = eval(input('Digite sua idade: '))

if idade > 62:
    print('Você pode obter benefícios de pensão')

##

# Exercicio b)

nome = input('Digite um nome: ')

lista = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']

if nome in lista:
    print(nome)
    print('Um dos 5 maiores jogadores de beisebol de todos os tempos!')

##

# Exercicio c)

golpes = eval(input('Quantos golpes recebeu? '))
defesas = eval(input('Quantas defesas foram feitas? '))

if golpes > 10 and defesas == 0:
    print('Você está morto...')

##

position = input('Onde você está? ')

location = ['norte', 'sul', 'leste', 'oeste']

if position in location:
    print('Posso escapar...')