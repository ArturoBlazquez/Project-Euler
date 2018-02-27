def digitSum(num):
    return sum([int(x) for x in str(num)])

max=0
for a in range(100):
    for b in range(100):
        if max<digitSum(a**b):
            max=digitSum(a**b)

print max

#972
