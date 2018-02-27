from random import randint

def getNextDistribution():
    global distribution2
    global distribution1
    
    aux=distribution2.copy()
    distribution2={}
    
    for i in range(min(aux.keys())+n,max(aux.keys())+m+1):
        suma=0
        minim=max(n,i-max(aux.keys()))
        maxim=min(m+1,i-min(aux.keys())+1)
        for j in range(minim,maxim):
            suma=suma+distribution0[j]*aux[i-j]
        distribution2[i]=suma
    
    aux=distribution1.copy()
    distribution1={}
    
    for i in range(min(aux.keys())+n,max(aux.keys())+m+1):
        suma=0
        minim=max(n,i-max(aux.keys()))
        maxim=min(m+1,i-min(aux.keys())+1)
        for j in range(minim,maxim):
            suma=suma+distribution0[j]*aux[i-j]
        distribution1[i]=suma

n=30
m=60
distribution0={}

tot=len(range(n,m+1))
for i in range(n,m+1):
    distribution0[i]=1.0/tot

distribution1=distribution0
distribution2=distribution0

sum=0
prevsum=10
for v in range(1,10000):
    getNextDistribution()
    
    for i in range(min(distribution1.keys()),max(distribution1.keys())+1):
        perc=0
        for j in range(i+6,max(distribution2.keys())+1):
            perc+=distribution1[i]*distribution2[j]
            sum=sum+(i+5*v)*distribution1[i]*distribution2[j]
        distribution1[i]-=perc
    print sum
    print "---"
    
    if sum!=0 and abs(sum-prevsum)<0.0001:
        break
    prevsum=sum
            
print sum
