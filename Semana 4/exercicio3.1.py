"""

Problema Prático 3.1

Implemente um programa que solicita a temperatura atual em graus Fahrenheit do usuário e
exibe a temperatura em graus Celsius usando a fórmula

    celsius = 5/9(fahrenheit - 32)

Seu programa deverá ser executado da seguinte forma:

# >>>
  Digite a temperatura em graus Fahrenheit: 50
  A temperatura em graus Celsius é 10.0

"""

fahrenheit = eval(input('Digite a temperatura em graus Fahrenheit: '))

celsius = (5/9) * (fahrenheit - 32)

print(f'A temperatura em graus Fahrenheit é {celsius}')
