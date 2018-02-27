def firstDigits(num):
    return num/100

def lastDigits(num):
    return num%100

def range_excluded(ini,end,excluded):
    rango=range(ini,end)
    for i in excluded:
        rango.remove(i)
    return rango


polig=[[],[],[],[],[],[],[],[],[]]

for n in range(1,200):
    polig[3].append((n*(n+1))/2)
    polig[4].append(n*n)
    polig[5].append((n*(3*n-1))/2)
    polig[6].append(n*(2*n-1))
    polig[7].append((n*(5*n-3))/2)
    polig[8].append(n*(3*n-2))

polig[3]=[x for x in polig[3] if x<10000 and x>999]
polig[4]=[x for x in polig[4] if x<10000 and x>999]
polig[5]=[x for x in polig[5] if x<10000 and x>999]
polig[6]=[x for x in polig[6] if x<10000 and x>999]
polig[7]=[x for x in polig[7] if x<10000 and x>999]
polig[8]=[x for x in polig[8] if x<10000 and x>999]


combinations=[[[] for x in range(9)] for x in range(9)]
for i in range(3,9):
    for j in range(3,9):
        for x in polig[i]:
            for y in polig[j]:
                if lastDigits(x)==firstDigits(y):
                    combinations[i][j].append(x)

combinations2=[[[] for x in range(9)] for x in range(9)]
for i1 in range(3,9):
    for i2 in range_excluded(3,9,[i1]):
        for i3 in range_excluded(3,9,[i1,i2]):
            for x1 in combinations[i1][i2]:
                for x2 in combinations[i2][i3]:
                    if lastDigits(x1)==firstDigits(x2):
                        for i4 in range_excluded(3,9,[i1,i2,i3]):
                            for x3 in combinations[i3][i4]:
                                if lastDigits(x2)==firstDigits(x3):
                                    for i5 in range_excluded(3,9,[i1,i2,i3,i4]):
                                        for x4 in combinations[i4][i5]:
                                            if lastDigits(x3)==firstDigits(x4):
                                                for i6 in range_excluded(3,9,[i1,i2,i3,i4,i5]):
                                                    for x5 in combinations[i5][i6]:
                                                        if lastDigits(x4)==firstDigits(x5):
                                                            for x6 in combinations[i6][i1]:
                                                                if lastDigits(x6)==firstDigits(x1) and lastDigits(x5)==firstDigits(x6):
                                                                    lista=[x1,x2,x3,x4,x5,x6]
                                                                    print "sum(",lista,")=",sum(lista)

#28684
