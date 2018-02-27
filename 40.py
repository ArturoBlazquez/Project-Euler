num='.'

for i in range(1,10**6):
    num+=str(i)
    if len(num)>10**6:
        break

tot=1
for i in range(0,7):
    tot*=int(num[10**i])

print tot

#210
