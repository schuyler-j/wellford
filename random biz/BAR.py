import time
import random

f = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']

y = []
z = []

def getran():
    global cor
    cor = 8
    for i in f:
        n = random.randint(0, 1)
        m = random.randint(0, 1)
        if n == m:
            cor = cor
        else:
            cor = cor - 1
        y.append(n)
        z.append(m)
    bar = cor / (8)
    print(bar * 100, "%") 

get = []
zz = 1
while zz > 0:
    getran()
    time.sleep(0.4)
    get.append(getran().bar)
    print(get)




