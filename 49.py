from euler import primes, isPrime
from itertools import permutations

def get_permutations(num):
    aux=str(num)
    for i in permutations(aux):
        yield ''.join(i)
    

primes=[x for x in primes(10000) if x>=1000]

for p in primes:
    current=[]
    for permut in get_permutations(p):
        perm=int(permut)
        if isPrime(perm) and perm not in current:
            current.append(perm)
            if len(current)==3:
                current=sorted(current)
                if current[1]-current[0]==current[2]-current[1]:
                    print str(current[0])+str(current[1])+str(current[2])

#296962999629
