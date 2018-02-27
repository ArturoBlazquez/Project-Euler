from euler import isPrime,range_infinite,primes

primes=primes(10**5)

for i in range_infinite(35,2):
    if not isPrime(i):
        flag=True
        for p in primes:
            if p<i:
                found=False
                for j in range_infinite(1,1):
                    if p+2*j*j>i:
                        break
                    elif p+2*j*j==i:
                        found=True
                        break
                if found:
                    break
            else:
                flag=False
                break
        if not flag:
            print i
            break

#5777
