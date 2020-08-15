"""

Problema Prático 2.4

Comece executando as instruções de atribuição

# >>> s1 = 'ant'
# >>> s2 = 'bat'
# >>> s3 = 'cod'

Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:

a) 'ant bat cod'

b) 'ant ant ant ant ant ant ant ant ant ant'

c) 'ant bat bat cod cod cod'

d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'

e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'

"""

print("s1 = 'ant'\ns2 = 'bat'\ns3 = 'cod'\n")
print('\n')

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# Letra a)
print("Exercicio a)\ns1 + ' ' + s2 + ' ' + s3\n", s1 + ' ' + s2 + ' ' + s3)
print('\n')

# Letra b)
print("Exercicio b)\n(s1 + ' ') * 9 + s1\n", (s1 + ' ') * 9 + s1)
print('\n')

# Letra c)
print("Exercicio c)\ns1 + ' ' + ((s2 + ' ') * 2) + ((s3 + ' ') * 2) + s3\n",
      s1 + ' ' + ((s2 + ' ') * 2) + ((s3 + ' ') * 2) + s3)
print('\n')

# Letra d)
print("Exercicio d)\n(s1 + ' ' + s2 + ' ') * 6 + (s1 + ' ' + s2)\n", (s1 + ' ' + s2 + ' ') * 6 + (s1 + ' ' + s2))
print('\n')

# Letra e)
print("Exercicio e)\n((s2 * 2) + s3 + ' ') * 4 + ((s2 * 2) + s3)\n", ((s2 * 2) + s3 + ' ') * 4 + ((s2 * 2) + s3))
