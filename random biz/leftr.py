import numpy as np
import matplotlib.pyplot as plt
import time
import random

#set the length as 8
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#empty lists
f = []
g = []
total = []
cor = 0
x = 0
def getran():
    for i in l:
        n = random.randint(0, 1)
        a = f.append(n)

    for i in l:
        m = random.randint(0, 1)
        b = g.append(m)

def check():
    for i in f:
        if i == g[i]:
            global cor 
            cor = cor + 1
            total.append(cor)
        else:
            cor = cor - 1
            total.append(cor)
    for i in g:
        if i == f[i]:
            cor = cor + 1 
            total.append(cor)
        else:
            cor = cor - 1
            total.append(cor)
        print (i)
    '''
    for i in f:
        if i == f[i]:
            cor = cor + 1 
            total.append(cor)
        else:
            cor = cor - 1
            total.append(cor)
        print (i)
 
    for i in g:
        if i == g[i]:
            cor = cor + 1 
            total.append(cor)
        else:
            cor = cor - 1
            total.append(cor)
        print (i)
    '''






getran()
check()
print (f)
print (g)
print (total)

N = total
x = np.random.randint(N)
y = total

plt.pcolormesh([x,y])
plt.show()

#extended loop (optimise???how?)
zz = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2]
'''
for i in zz:
    getran()
    if i == 1:
        print(f)
        time.sleep(0.4)

    else:
        print(g)
        check()
'''







