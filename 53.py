from math import factorial

def combinatorial(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

big=[]
for n in range(1,101):
    for r in range(1,n):
        if combinatorial(n,r)>10**6:
            big.append(n)

print len(big)

#4075
