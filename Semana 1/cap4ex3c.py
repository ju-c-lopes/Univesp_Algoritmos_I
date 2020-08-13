"""
Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno
representadas pelas variáveis N1, N2, N3 e N4.
Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem “Aprovado”
se a média obtida for maior ou igual a 5; caso contrário,
apresentar a mensagem “Reprovado”.
Informar também, após a apre-sentação das mensagens, o valor da média obtida pelo aluno
"""

n1, n2, n3, n4 = 8.0, 6.8, 9.5, 7.0

md = (n1 + n2 + n3 + n4) / 4

ex = """n1, n2, n3, n4 = 8.0, 6.8, 9.5, 7.0

md = (n1 + n2 + n3 + n4) / 4

if md >= 5:
    print("Aprovado")
else:
    print("Reprovado") \n\n"""

print(ex)

if md >= 5:
    print("Aprovado")
else:
    print("Reprovado")

print("Média obtida pelo aluno = ", md)

