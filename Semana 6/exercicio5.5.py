"""

Problema Prático 5.5

Um acrônimo é uma palavra formada tornando-se as primeiras letras das palavras em uma
frase e depois criando uma palavra para elas. Por exemplo, RAM é um acrônimo para a
memória de acesso aleatório (random access memory). Escreva uma função acrônimo() que
aceite uma frase (ou seja, uma string) como entrada e depois retorne o acrônimo para
essa frase. Nota: O acrônimo deverá estar em letras maiúsculas, mesmo que as palavras
na frase não sejam iniciadas por maiúsculas.

# >>> acrônimo('Random access memory')
  'RAM'
# >>> acrônimo('central processing unit')
  'CPU'

"""


def acronimo(texto):
    """
    Pegará a primeira letra de cada palavra da string informada e retornará
    suas iniciais em letra maiúscula.
    """
    acr = []
    texto = texto.split()
    for i in texto:
        acr.append(i[0])
    new_word = ''.join(acr)
    new_word = new_word.upper()
    return new_word

