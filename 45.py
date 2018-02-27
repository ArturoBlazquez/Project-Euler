triangs=[]
pentags=[]
hexags=[]

num=200000

for i in range(1,int(num*2)):
    triangs.append((i*(i+1))/2)

for i in range(1,int(num*1.2)):
    pentags.append((i*(3*i-1))/2)

for i in range(1,num):
    hexags.append(i*(2*i-1))

triangs=sorted(set(triangs))
pentags=sorted(set(pentags))
hexags=sorted(set(hexags))

print "max hexagonal =",hexags[-1]
print "max pentagonal=",pentags[-1]
print "max triangular=",triangs[-1]


for i in hexags:
    if i in pentags and i in triangs:
        print i

#1533776805
