"""

Problema Prático 2.8

Em que ordem os operadores nas expressões a seguir são avaliados?

a) 2 + 3 == 4 or a >= 5

    R:) 1° -> operador + na expressão 2 + 3
        2° -> comparadores == e >=

        OBS: o próximo e último que seria avaliado seria o operador or, porém a variável a não havia sido definida,
            retornando então um NameError

b) lst[1] * -3 < -10 == 0

    OBS: a lista lst não foi definida, ignorando esse fato, as ordem seriam:

    R:) 1° -> verifica a o item da lista no index 1
        2° -> avaliaria os números negativos
        3° -> efetuaria a multiplicação *
        4° -> compararia se o resultado da expressão list[1] * 3 é menor que -10
        5° -> finalizaria avaliando se toda essa expressão é igual a 0

c) (lst[1] * -3 < -10) in [0, True]

    R:) 1° -> avalia a expressão entre parenteses ()
        2° -> verifica o item na lista lst no index 1
        3° -> avalia número negativo -3
        4° -> efetua a multiplicação de lst[1] e 3
        5° -> compara se o resultado da expressão lst[1] * 3 é menor que -10
        6° -> Verifica se o resultado de toda expressão do parenteses está contido na lista [0, True]

    Concluindo: a saída final será True, pois na lista [0, True] o 0 é interpretado como False, logo,
                qualquer resultado booleano seria avaliado como True

d) 2 * 3**2

    R:) 1° -> é feito a potência de 3 elevado ao quadrado, resultando 9
        2° -> é feito a multiplicação do resultado 9 e 2, finalizando na saída em 18


e) 4 / 2 in [1, 2, 3]

    R:) 1° -> será feito a divisão de 4 e 2, resultando em um número float 2.0
        2° -> verifica se o resultado obtido está na lista [1, 2, 3]

    Conclusão: a saída final é True pois mesmo a divisão indicando um resultado float
                a expressão 2.0 == 2 é avaliada como True e 2 está na lista [1, 2, 3]

"""