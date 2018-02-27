from euler import primes,range_infinite

def numSums(top,list):
    if len(list)<1 or top<0:
        return 0
    elif top==0:
        return 1
    else:
        ret=0
        max=len(list)
        for i in reversed(list):
            ret+=numSums(top-i,list[0:max])
            max-=1
        return ret

for i in range_infinite(4):
    prim=primes(i)
    if numSums(i,prim)>5000:
        print i
        break

#71
