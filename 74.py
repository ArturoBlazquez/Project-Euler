from math import factorial
from euler import get_digit

dict={}

for n in range(1,10**6):
    if n not in dict:
        now=[n]
        chain=1
        while 1:
            next=0
            for i in range(0,len(str(now[-1]))):
                next+=factorial(get_digit(now[-1],i))
            if next in now:
                break
            if next in dict:
                chain+=dict[next]
                break
            now.append(next)
            chain+=1
        for i in now:
            if i not in dict:
                dict[i]=chain-now.index(i)

print len([(x,y) for x,y in dict.items() if x<10**6 and y==60])

#402
