"""

Problema Prático 4.3

Escreva uma instrução que exibe os valores das variáveis último, primeiro e meio
em uma linha, separadas por um caractere de tabulação horizontal. (A sequência de
escape Python para o caractere de tabulação horizontal é \t.) Se as variáveis são
atribuídas desta forma:

# >>> último = 'Smith'
# >>> primeiro = 'John'
# >>> meio = 'Paul'

a saída deverá ser:

Smith   John   Paul

"""

ultimo = 'Smith'
primeiro = 'John'
meio = 'Paul'

print(ultimo, primeiro, meio, sep='\t')
