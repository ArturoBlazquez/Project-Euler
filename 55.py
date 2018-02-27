def isPalindromic(num):
    return str(num)==str(num)[::-1]

def nextLycherel(num):
    return num+int(str(num)[::-1])

def isLycherel(num):
    for i in range(49):
        num=nextLycherel(num)
        if isPalindromic(num):
            return False
    return True

lych=[]
for i in range(1,10000):
    if isLycherel(i):
        lych.append(i)

print len(lych)

#249
