import random

f = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
cor = 80

y = []
z = []

for i in f * 10:
    n = random.randint(0, 1)
    m = random.randint(0, 1)
    if n == m:
        cor = cor
    else:
        cor = cor - 1
    y.append(n)
    z.append(m)
    print(y)
    print(z)

bar = cor / 80

print(bar * 100, "%")

print(cor)

print(len(y))
