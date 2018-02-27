from euler import range_infinite

def hasSameDigits(num1,num2):
    return sorted(list(str(num1)))==sorted(list(str(num2)))

for i in range_infinite(1):
    if hasSameDigits(i,2*i) and hasSameDigits(i,3*i) and hasSameDigits(i,4*i) and hasSameDigits(i,5*i) and hasSameDigits(i,6*i):
        print i,2*i,3*i,4*i,5*i,6*i
        break

#142857
