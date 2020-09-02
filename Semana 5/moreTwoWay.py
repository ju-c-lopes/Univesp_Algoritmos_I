def temperatura(t):
    """Exibe mensagem com base no valor de temperatura t"""
    if t > 86:
        print('Está quente!')
    elif t > 32:
        print('Está frio.')
    else:
        print('Está congelando!')


temperatura(52)
