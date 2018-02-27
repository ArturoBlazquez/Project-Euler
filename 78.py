"""
De la formula (4) http://mathworld.wolfram.com/PartitionFunctionPCongruences.html sacamos la formula para generar los que son divisibles por 5^6
Resolvemos http://www.wolframalpha.com/input/?i=24n%3D5%5E6*k%2B1, y sacamos que tenemos que comprobar n=15625m + 14974
De la formula vamos viendo si tambien es divisible por 2^6"""

"""
maxm=0;
For[m=177,True,m++,If[Divisible[PartitionsP[15625m + 14974],2^6],Print[15625m + 14974];Break[]];maxm=m]
maxm

Nos da 2858724, pero vemos que no. Buscamos la formula de p(n) en wikipedia, la optimizamos y en python 
"""

from euler import range_infinite
from math import sqrt,ceil

partition={0:1}

def p(n):
    if n<0:
        return 0
    elif n in partition:
        return partition[n]
    else:
        ret=0
        r=range(int(ceil(-(sqrt(24*n+1)-1)/6)),int((sqrt(24*n+1)+1)/6)+1)
        r.remove(0)
        for k in r:
            ret+=(-1)**(abs(k)-1)*p(n-(k*(3*k-1))/2)
        ret=ret%10**6
        if n not in partition:
            partition[n]=ret
        return ret


for i in range_infinite():
    if p(i)==0:
        print i
        break

#55374
