"""

Problema Prático 5.4

Implemente a função fatorial(), que toma como entrada um inteiro não negativo e retorna
seu fatorial. O fatorial de um inteiro não negativo n, indicado por n!, é definido desta maneira:

    n! =         1                                  se n=0
            {    n x (n-1) x (n-2) x ... x 2 x 1    se n>0


Logo, 0! = 1, 3! = 6 e 5! = 120

# >>> fatorial(0)
  1
# >>> fatorial(3)
  6
# >>> fatorial(5)
  120

"""


def fatorial(n):
    """
    Calcula o Fatorial de um número
    """
    fator = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            fator *= i
    return fator
