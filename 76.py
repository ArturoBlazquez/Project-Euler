tot=100

def numSums(suma,maxnum):
    if suma==0 or suma==1 or maxnum==1:
        return 1
    if maxnum==2:
        return suma/2+1
    else:
        ret=0
        for i in range(min(suma,maxnum),0,-1):
            ret+=numSums(suma-i,i)
        return ret

sum=0
for i in range(tot-1,0,-1):
    sum+=numSums(tot-i,i)

print sum

#190569291

#En mathematica es PartitionsP[100]-1
