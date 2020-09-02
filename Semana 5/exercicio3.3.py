"""

Problema Prático 3.3

Traduza as declarações em instrições if/else do Python:

a) se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário,
exiba 'Definitivamente não é um ano bissexto.'

b) Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba
'Melhor sorte da próxima vez...'

"""
##

# Exercicio a)

ano = eval(input('Digite um ano: '))

if ano % 4 == 0:
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')

##

# Exercicio b)

loteria = [1, 3, 9, 18, 35, 41]

bilhete = list()

for i in range(0, 6):
    num = eval(input('Digite a sequencia de números do seu bilhete: '))
    bilhete.append(num)

if bilhete == loteria:
    print('Voce ganhou!')
else:
    print('Melhor sorte da próxima vez...')
