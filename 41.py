from euler import isPrime
from itertools import permutations

nums=[]

def getPermutations(perm):
    for i in permutations(perm):
        yield ''.join(i)
        
for i in range(1,10):
    nums.append(str(i))
    for perm in getPermutations(nums):
        if isPrime(int(perm)):
            max=perm

print max

#7652413
