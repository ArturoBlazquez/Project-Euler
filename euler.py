from itertools import count
import numpy as np
from itertools import permutations
from math import factorial,sqrt,ceil

"""
import time

start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))
"""

                                         # ideone.com/aVndFM
def primes_iterable():                   # postponed sieve, by Will Ness      
    yield 2; yield 3; yield 5; yield 7;  # original code David Eppstein, 
    sieve = {}                           #   Alex Martelli, ActiveState Recipe 2002
    ps = primes_iterable()               # a separate base Primes Supply:
    p = next(ps) and next(ps)            # (3) a Prime to add to dict
    q = p*p                              # (9) its sQuare 
    for c in count(9,2):                 # the Candidate
        if c in sieve:               # c's a multiple of some base prime
            s = sieve.pop(c)         #     i.e. a composite ; or
        elif c < q:  
             yield c                 # a prime
             continue              
        else:   # (c==q):            # or the next base prime's square:
            s=count(q+2*p,2*p)       #    (9+6, by 6 : 15,21,27,33,...)
            p=next(ps)               #    (5)
            q=p*p                    #    (25)
        for m in s:                  # the next multiple 
            if m not in sieve:       # no duplicates
                break
        sieve[m] = s                 # original test entry: ideone.com/WFv4f

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

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

def get_digit(number, n):
    return number // 10**n % 10

def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        for v in m : yield v
        m = np.dot(m, uad)

def pythagorean_triplets(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim

def range_infinite(start=0, incr=1):
    index=start
    while 1:
        yield index
        index += incr

def combinatorial(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

partition={0:1}

def partitions(n):
    if n<0:
        return 0
    elif n in partition:
        return partition[n]
    else:
        ret=0
        r=range(int(ceil(-(sqrt(24*n+1)-1)/6)),int((sqrt(24*n+1)+1)/6)+1)
        r.remove(0)
        for k in r:
            ret+=(-1)**(abs(k)-1)*partitions(n-(k*(3*k-1))/2)
        if n not in partition:
            partition[n]=ret
        return ret

def validRomanToInt(num):
    roman=num[::-1]
    
    ret=0
    
    for i in range(4):
        if roman[0]=='I':
            ret+=1
            roman=roman[1:]
            if roman=='':
                return ret
        
    if roman[0:2]=='VI':
        ret+=4
        roman=roman[2:]
        if roman=='':
            return ret
    elif roman[0]=='V':
        ret+=5
        roman=roman[1:]
        if roman=='':
            return ret
    
    if roman[0:2]=='XI':
        ret+=9
        roman=roman[2:]
        if roman=='':
            return ret
    
    
    for i in range(4):
        if roman[0]=='X':
            ret+=10
            roman=roman[1:]
            if roman=='':
                return ret
    
    if roman[0:2]=='LX':
        ret+=40
        roman=roman[2:]
        if roman=='':
            return ret
    elif roman[0]=='L':
        ret+=50
        roman=roman[1:]
        if roman=='':
            return ret
    
    if roman[0:2]=='CX':
        ret+=90
        roman=roman[2:]
        if roman=='':
            return ret
    
    
    for i in range(4):
        if roman[0]=='C':
            ret+=100
            roman=roman[1:]
            if roman=='':
                return ret
    
    if roman[0:2]=='DC':
        ret+=400
        roman=roman[2:]
        if roman=='':
            return ret
    elif roman[0]=='D':
        ret+=500
        roman=roman[1:]
        if roman=='':
            return ret
    
    if roman[0:2]=='MC':
        ret+=900
        roman=roman[2:]
        if roman=='':
            return ret
    
    
    for i in range(4):
        if roman[0]=='M':
            ret+=1000
            roman=roman[1:]
            if roman=='':
                return ret
    return ret


def intToRoman(num):
    ret=''
    
    while num>=1000:
        ret+='M'
        num-=1000
    
    
    if num>=900:
        ret+='CM'
        num-=900
    elif num>=500:
        ret+='D'
        num-=500
    elif num>=400:
        ret+='CD'
        num-=400
    
    while num>=100:
        ret+='C'
        num-=100
    
    
    if num>=90:
        ret+='XC'
        num-=90
    elif num>=50:
        ret+='L'
        num-=50
    elif num>=40:
        ret+='XL'
        num-=40
    
    while num>=10:
        ret+='X'
        num-=10
    
    
    if num>=9:
        ret+='IX'
        num-=9
    elif num>=5:
        ret+='V'
        num-=5
    elif num>=4:
        ret+='IV'
        num-=4
    
    while num>=1:
        ret+='I'
        num-=1
    
    return ret
