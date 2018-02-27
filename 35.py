circulars=[]

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def isprime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def rotations(num):
    rots=[]
    aux=str(num)
    for i in range(1,len(aux)):
        aux=aux[-1]+aux[0:-1]
        rots.append(int(aux))
    return rots

for i in primes(10**6):
    flag=True
    for j in rotations(i):
        if flag and not isprime(j):
            flag=False
    if flag:
        circulars.append(i)

print len(circulars)

#55
