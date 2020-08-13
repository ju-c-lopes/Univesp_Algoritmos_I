"""

4a) Ler uma temperatura em graus Celsius e apresentá-la convertida emgraus Fahrenheit. A fórmula de conversão é
F <- C * 9 / 5 + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

celsius = 28
fahr = ((celsius * 9) / 5) + 32

ex = """celsius = 28\nfahr = ((celsius * 9) / 5) + 32"""

print(ex, "\n{}° C equivale a {}° F".format(celsius, fahr))
