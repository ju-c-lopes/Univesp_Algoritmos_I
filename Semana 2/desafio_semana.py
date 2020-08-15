n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media < 5:
    print("Média = ", media)
    print("Aluno Reprovado")
else:
    print("Média = ", media)
    print("Aluno Aprovado")
