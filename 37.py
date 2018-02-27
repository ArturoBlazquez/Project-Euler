from euler import primes,isPrime

truncatables=[]

def truncatableLeft(a):
    num=str(a)
    while len(num)>1:
        num=num[1:]
        if not isPrime(int(num)):
            return False
    return True


def truncatableRight(a):
    num=str(a)
    while len(num)>1:
        num=num[:-1]
        if not isPrime(int(num)):
            return False
    return True


for i in primes(10**6):
    if truncatableLeft(i) and truncatableRight(i) and i>10:
        truncatables.append(i)
        if len(truncatables)>11:
            break


print sum(truncatables)

#748317
