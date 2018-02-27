from itertools import permutations

sum=0

def getPermutations(perm):
    for i in permutations(perm):
        yield ''.join(i)

for perm in getPermutations(['0','1','2','3','4','5','6','7','8','9']):
    if int(perm[1:4])%2==0 and int(perm[2:5])%3==0 and int(perm[3:6])%5==0:
        if int(perm[4:7])%7==0 and int(perm[5:8])%11==0 and int(perm[6:9])%13==0:
            if int(perm[7:10])%17==0:
                sum+=int(perm)

print sum

#16695334890
