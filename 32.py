from itertools import permutations

nums=['1','2','3','4','5','6','7','8','9']
prods=[]

def getPermutations(perm):
    for i in permutations(perm):
        yield ''.join(i)
        

for perm in getPermutations(nums):
    for i in range(1,len(nums)-1):
        for j in range(i+1,len(nums)):
            if int(perm[0:i])*int(perm[i:j])==int(perm[j:]):
                if int(perm[j:]) not in prods:
                    prods.append(int(perm[j:]))

print sum(prods)

#45228
