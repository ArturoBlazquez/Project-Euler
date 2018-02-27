from fractions import Fraction

iteration=[Fraction(1,2)]

def getIterations(n):
    if len(iteration)<n:
        iteration.append(Fraction(1,2+iteration[n-2]))

for i in range(1,1001):
    getIterations(i)

bigger=[]
for i in range(1,1001):
    expansion=1+iteration[i-1]
    if len(str(expansion.numerator))>len(str(expansion.denominator)):
        bigger.append(i)

print len(bigger)

#153
