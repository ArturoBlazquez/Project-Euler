from math import sqrt

pentags=[]

max=10000

def isPentag(num):
    doub=(sqrt(24*num+1.0)+1)/6.0
    return doub==int(doub)

for i in range(1,max*2):
    pentags.append((i*(3*i-1))/2)


for i in range(0,max):
    for j in range(0,max):
        if isPentag(pentags[i]+pentags[j]) and isPentag(abs(pentags[i]-pentags[j])):
            print pentags[i],pentags[j]
            print pentags[i]+pentags[j], abs(pentags[i]-pentags[j])

#5482660
