from euler import primes,isPrime

primes=primes(10**6)
realmax=0
for c in range(2,1000):
    max=0
    for i in range(0,len(primes)):
        tot=sum(primes[i:i+c])
        if tot>10**6:
            break
        elif isPrime(tot):
            if max<tot:
                max=tot

    if max>0:
        realmax=max

print realmax

#997651
