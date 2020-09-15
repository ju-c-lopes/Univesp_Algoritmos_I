##

s = 'algoritmos'

for c in s:
    if c in 'aeiou':
        print(c)

##

l = ['cão', 'gato', 'coelho']

for i in l:
    print(i)

##

for x in range(10):
    print(x)

##

for y in range(1, 20, 2):
    print(y)

##

l = ['a', 'b', 'c']

for i in range(len(l)):
    print(l[i])

##
acum = 0

for x in range(1, 101):
    if x % 2 == 0:
        acum = acum + x
print(acum)

##

str_list = ['João', 'Roberto', 'Rafael']

for nome in str_list:
    for c in nome:
        if c in 'aeiou':
            print(c)
