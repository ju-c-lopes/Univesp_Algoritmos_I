"""

Problema Prático 3.13

Suponha que uma lista não vazia time foi atribuida. Escreva uma instrução Python ou instruções que
mapeiam o primeiro e o último valor da lista. Assim, se a lista original for:

# >>> time = ['Ava', 'Eleanor', 'Clare', 'Sarah']

então a lista resultante deverá ser:

# >>> time
  ['Sarah', 'Eleanor', 'Clare', 'Ava']

"""

time = ['Ava', 'Eleanor', 'Clare', 'Sarah']

time[0], time[-1] = time[-1], time[0]
