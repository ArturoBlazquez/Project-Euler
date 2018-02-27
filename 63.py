from euler import range_infinite

res=0
for i in range_infinite(1):
    for j in range_infinite(1):
        if len(str(j**i))==i:
            print j,"^",i,"=",j**i
            res+=1
        if len(str(j**i))>i:
            break
    if i>1000: break

print res

#49
