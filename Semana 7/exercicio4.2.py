"""

Problema Prático 4.2

Supondo que a variável previsão tenha recebido a string

    'It will be a sunny day today'

escreva instruções Python correspondentes a estas atribuições:

a) À variável cont, a quantidade de ocorrências da string 'day' na string previsão.

b) À variável clima, o índice em que a substring 'sunny' começa.

c) À variável troca, uma cópia de previsão na qual cada ocorrência da substring 'sunny'
é substituida por 'cloudy'.

"""

previsao = 'It will be a sunny day today'

# a)

cont = previsao.count('day')
print(cont)

# b)

clima = previsao.find('sunny')
print(clima)

# c)

troca = previsao.replace('sunny', 'cloudy')
print(troca)

