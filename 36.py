palindromes=[]
tot=[]

for i in range(1,10**6):
    if str(i)==str(i)[::-1]:
        palindromes.append(i)


for i in palindromes:
    binary=bin(i)[2:]
    if binary==binary[::-1]:
        tot.append(i)

print sum(tot)

#872187
