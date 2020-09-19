"""

Problema Prático 4.5

Suponha que as variáveis primeiro, último, rua, número, cidade, estado, codPostal já tenham
sido atribuídas. Escreva uma instrução print que crie uma etiqueta de correspondência:

    John Doe
    123 Main Street
    AniCity, AS 09876

supondo que:

# >>> primeiro = 'John'
# >>> último = 'Doe'
# >>> rua = 'Main Street'
# >>> número = 123
# >>> cidade = 'AnyCity'
# >>> estado = 'AS'
# >>> codPostal = '09876'

"""

primeiro = 'John'
ultimo = 'Doe'
rua = 'Main Street'
numero = 123
cidade = 'AnyCity'
estado = 'AS'
codPostal = '09876'

print('{0} {1}\n{2} {3}\n{4}, {5} {6}'.format(primeiro, ultimo, numero, rua, cidade, estado, codPostal))
