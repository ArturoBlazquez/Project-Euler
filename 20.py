from math import factorial

def get_digit(number, n):
    return number // 10**n % 10

sum=0
f=factorial(100)
for i in range(len(str(f))):
    sum+=get_digit(f,i)
print sum

#648
