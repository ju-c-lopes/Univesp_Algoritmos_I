"""

Exemplo

Calcule a média harmônica dos seguintes números: 3.6, 8.9, 10

A média harmônica é definida pela equação:

H =     N
    __________
    Σ  N   1
      i=1 ____
           Ni

"""
##

3/((1/3.6)+(1/8.9)+(1/10))
##

"""

Exercicio

Modifique o exemplo anterior para calcular a média harmônica amortizada
dos mesmos números: 3.6, 8.9 e 10.
Utilize X = 4 como fator de amortização

H =      N
    ____________ - X
    Σ  N     1
      i=1 ______
          Ni + X

"""
##

3 / (((1 / (3.6 + 4)) + (1 / (8.9 + 4)) + (1 / (10 + 4))) - 4)
##