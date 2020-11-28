import time
import random

#set the length as 8
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#empty lists
f = []
g = []
total = []
global cor
cor = 0
def getran():
    for i in l:
        n = random.randint(0, 1)
        a = f.append(n)

    for i in l:
        m = random.randint(0, 1)
        b = g.append(m)

def check():
    for i in f:
        if f[i] == g[i]:
            global cor 
            cor = cor + 1
            total.append(i)
        else:
            pass
    for i in g:
        if g[i] == f[i]:
            cor = cor - (i*8)
            total.append(i)
        else:
            pass

    print (len(total))
'''
getran()
check()
print (f)
print (g)
'''


#extended loop (optimise???how?)
zz = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2]
for i in zz:
    getran()
    if i == 1:
        print(f)
        time.sleep(0.4)

    else:
        print(g)
        check()
