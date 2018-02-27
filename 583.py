import time
from operator import itemgetter
from math import sqrt

start_time = time.time()

max=10**7
maxim=max*2

import numpy as np

def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        for v in m : yield v
        m = np.dot(m, uad)

def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim

#tripa = list(gen_all_pyth_trips(max))
tripa = [x for x in gen_all_pyth_trips(maxim) if x[0]<max and x[1]<max and x[2]<max]
print "a triangles"
tripb = [[x[1],x[0],x[2]] for x in tripa]
print "b triangles"

trips = sorted(tripa+tripb, key=itemgetter(0,1,2))
print "triangles sorted"

del tripa
del tripb


equals = []
sum=0
for i in range(len(trips)-1):
    if trips[i][0]*2>max:
        break
    
    if trips[i][0]==trips[i+1][0]:
        equals.append(trips[i])
    else:
        equals.append(trips[i])
        #operate
        num=len(equals)
        if num>1:
            for j in range(0,num):
                for k in range(j+1,num):
                    h = equals[j][1]
                    x = equals[j][0]*2
                    y = equals[k][1]-h
                    if y>h and sqrt(x*x+y*y).is_integer():
                        perim = x+2*y+2*equals[j][2]
                        if perim<=max:
                            sum+=perim
                            #print x,y,equals[j][2]
        equals = []

print sum

print("--- %s seconds ---" % (time.time() - start_time))

#1174137929000
