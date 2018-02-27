from sets import Set

def sum_of_factors(x):
    return sum([n for n in range(1,x) if x % n == 0])
    
abundant=[]
for i in range(28124):
    if sum_of_factors(i)>i:
        abundant.append(i)

print len(abundant)

max=len(abundant)
nums = Set()

for i in range(0,max):
    for j in range(i,max):
        if abundant[i]+abundant[j]>28123:
            break
        nums.add(abundant[i]+abundant[j])

print sum(range(1,28124))-sum(nums)

#4179871
