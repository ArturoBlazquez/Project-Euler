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

trips=[sum(x) for x in gen_all_pyth_trips(1500000) if sum(x)<=1500000]
trips=sorted(trips)

print "trips done"

total=0
i=0
while i < len(trips):
    if trips[i]==trips[i+1]:
        i+=1
        while i<len(trips) and trips[i]==trips[i-1]:
            i+=1
    else:
        total+=1
        i+=1

print total

#161667
