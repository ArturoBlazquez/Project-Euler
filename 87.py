from euler import primes

top=5*10**7

primes=primes(top)

primes1=[x for x in primes if x*x<top]
primes2=[x for x in primes1 if x*x*x<top]
primes3=[x for x in primes2 if x*x*x*x<top]

list=[]
for p1 in primes1:
    for p2 in primes2:
        for p3 in primes3:
            if p1**2+p2**3+p3**4<top:
                list.append(p1**2+p2**3+p3**4)

print len(set(list))

#1097343
