fib = [1,2]
for i in range(100000):
    next = fib[-1]+fib[-2]
    if next >= 4000000:
        break
    else:
        fib.append(next)

print sum([x for x in fib if x%2==0])

#4613732
