from euler import isPrime, primes
from itertools import combinations

def getCombinations(num):
    lista=range(len(str(num)))
    ret=[]
    for L in range(1, len(lista)+1):
        for subset in combinations(lista, L):
            ret.append(subset)
    return ret

def numPrimes(lista):
    return len([x for x in lista if isPrime(x)])

def getReplaced(num):
    ret=[]
    for c in getCombinations(num):
        ret.append(replace(num,c))
    return ret

def replace(num,pos):
    ret=[]
    if 0 in pos:
        lista=range(1,10)
    else:
        lista=range(10)
    for n in lista:
        aux=list(str(num))
        for p in pos:
            aux[p]=str(n)
        ret.append(int(''.join(aux)))
    return ret
            

for p in primes(10**6):
    stop=False
    for l in getReplaced(p):
        if numPrimes(l)==8:
            print l
            stop=True
            break
    if stop:
        break

#121313
