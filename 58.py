from euler import range_infinite,isPrime

total=1
primes=0
for n in range_infinite(3,2):
    total+=4
    if isPrime((n-2)*(n-2)+n-1):
        primes+=1
    if isPrime((n-1)*(n-1)+1):
        primes+=1
    if isPrime((n-1)*(n-1)+n):
        primes+=1
    
    if (primes+0.0)/total<0.1:
        print n
        break

#26241
