import time
import random

#set the length as 8
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#empty lists
f = []
g = []

correct = 0

def getran():
    for i in l:
        n = random.randint(0, 1)
        a = f.append(n)

    for i in l:
        m = random.randint(0, 1)
        b = g.append(m)

def check():
    correct = 0
    i = 0
    if f[i] == g[i]:
        correct = correct + 1
'''
def check1():
    i = 1
    if f[i] == g[i]:
        correct = correct + 1
def check2():
    i = 2
    if f[i] == g[i]:
        correct = correct + 1
def check3():
    i = 3
    if f[i] == g[i]:
        correct = correct + 1
def check4():
    i = 4
    if f[i] == g[i]:
        correct = correct + 1
def check5():
    i = 5
    if f[i] == g[i]:
        correct = correct + 1
def check6():
    i = 6
    if f[i] == g[i]:
        correct = correct + 1
def check7():
    if f[i] == g[i]:
        correct = correct + 1
'''


getran()
check()
'''
check1()
check2()
check3()
check4()
check5()
check6()
check7()
'''
print (correct)
print (f)
print (g)


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
        time.sleep(2)
    else:
        print(g)
w!
'''





