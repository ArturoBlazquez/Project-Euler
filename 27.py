def isPrime(n):
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

max=0
ab=0
for a in range(-999,1000):
    for b in range(-1000,1001):
        n=0
        tot=0
        while isPrime(n**2+a*n+b):
            tot+=1
            n+=1
        if tot>max:
            max=tot
            ab=a*b

print ab

#-59231
