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
        f.append(n)

    for i in l:
        m = random.randint(0, 1)
        g.append(m)

def check():
    i = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in f:
        for i in g:

            global cor 
            cor = cor + 1
            total.append(cor)
        else:
            cor = cor - 1
            total.append(cor)



    for i in f:
        if g[i] == f[i]:
            cor = cor - 1
            total.append(cor)
        else:
            cor = cor + 1
            total.append(cor)
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
#x = np.random.randint(N)
x = total
y = total

plt.pcolormesh([x,y])
plt.show()

'''
z = 1

#extended loop (optimise???how?)
#while seems slower

while z > 0:
    for i in range(1, 2):
        getran()
        if i == 1:
            print(f)
            time.sleep(0.5)

        else:
            print(g)
            check()
'''






