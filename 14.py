def Collatz(n):
    if n==1:
        return 1
    
    if n%2==0:
        return 1+Collatz(n/2)
    else:
        return 1+Collatz(3*n+1)

max=0

for i in range(1,1000000):
    if Collatz(i)>max:
        max=Collatz(i)
        num=i

print num
print max

#837799
