from euler import range_infinite

def products(n, min_divisor=2):
    """Generate expressions of n as a product of ints >= min_divisor."""
    if n == 1:
        yield []
    for divisor in range(min_divisor, n+1):
        if n % divisor == 0:
            for product in products(n // divisor, divisor):
                yield product + [divisor]
max=12000
prodSums={}

for i in range_infinite(4):
    for p in products(i):
        k=i+len(p)-sum(p)
        if k>=2 and k<=max and k not in prodSums:
            prodSums[k]=i
    if len(prodSums)==max-1:
        break

print sum(set(prodSums.values()))

#7587457
