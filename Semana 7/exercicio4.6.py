"""

Problema Prático 4.6

Implemente a função rol(), que recebe uma lista contendo informações de estudantes e
exibe um rol, como vemos a seguir. As informações do estudante, consistindo em seu
sobrenome, nome, nível e nota média, serão armazenadas nessa ordem em uma lista.
Portanto, a lista de entrada é uma lista de listas. Cuide para que o rol exibido
tenha 10 espaços para cada valor de string e 8 para a nota, incluindo 2 espaços para
a parte decima.

# >>> estudantes = []
# >>> estudantes.append(['DeMoines', 'Jim','Pleno', 3.45])
# >>> estudantes.append(['Pierre', 'Sophie', 'Pleno', 4.0])
# >>> estudantes.append(['Columbus', 'Maria', 'Sênior', 2.5])
# >>> estudantes.append(['Phoenix', 'River', 'Júnior', 2.45])
# >>> estudantes.append(['Olympia', 'Edgar', 'Júnior', 3.99])
# >>> rol(estudantes)

Último     Primeiro    Classe     Nota Média
Demoines   Jim         Pleno        3.45
Pierre     Sophie      Pleno        4.00
Columbus   Maria       Sênior       2.50
Phoenix    River       Júnior       2.45
Olympia    Edgar       Júnior       3.99

"""


def rol(lista):
    print('Último    Primeiro  Classe    Nota Média')
    n = len(lista)
    for i in range(0, n):
        print('{0:10}{1:10}{2:10}{3:5.2f}'.format(lista[i][0], lista[i][1], lista[i][2], lista[i][3]))


estudantes = list()
estudantes.append(['DeMoines', 'Jim', 'Pleno', 3.45])
estudantes.append(['Pierre', 'Sophie', 'Pleno', 4.00])
estudantes.append(['Columbus', 'Maria', 'Sênior', 2.50])
estudantes.append(['Phoenix', 'River', 'Júnior', 2.45])
estudantes.append(['Olympia', 'Edgar', 'Júnior', 3.99])
rol(estudantes)
