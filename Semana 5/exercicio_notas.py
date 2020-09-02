n1 = input('Digite a primeira nota: ')
n2 = input('Digite a segunda nota: ')

n1 = eval(n1)
n2 = eval(n2)

media = 0.4 * n1 + 0.6 * n2

if media >= 5.0:
    print(f'A média final foi {media:.2f}\nAPROVADO!!!')
else:
    print(f'A média final foi {media:.2f}\nREPROVADO!!!')
