"""

Problema Prático 2.10

Escreva expressões Python correspondentes ao seguinte:

a) O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados tem comprimentos a e b.

b) O valor da expressão que avalia se o comprimento da hipotenusa acima é 5.

c) A área de um disco com o raio a.

d) O valor da expressão booleana que verifica se um ponto com coordenadas x e y está dentro de um círculo
com centro (a, b) e raio r.

"""
import math

ca = 3
co = 4
hip = math.sqrt((ca**2) + (co**2))

print(f'Exercicio a)\nCA = {ca}, CO = {co}, Hipotenusa = {hip}')
print('\n')

print('Exercicio b)\nA hipotenusa é maior que 5? ', hip > 5, ', valor = ', hip)
print('\n')

raioA = 8
areaDisco = math.pi * (raioA ** 2)

print(f'Exercicio c)\nRaio (a) = {raioA}, Área do disco é = {areaDisco}')
print('\n')

a, b = 2, 6
r = b - a

x, y = 5, 3

print('Exercicio d)\n(x-a)**2 + (y-b)**2 < r**2', (x-a)**2 + (y-b)**2 < r**2)
