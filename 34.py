from math import factorial

curious=[]

def get_digit(number, n):
    return number // 10**n % 10

for i in range(3,1000000):
    tot=0
    for j in range(0,len(str(i))):
        tot+=factorial(get_digit(i, j))
    
    if tot==i:
        curious.append(i)
    
    tot=0

print sum(curious)

#40730
