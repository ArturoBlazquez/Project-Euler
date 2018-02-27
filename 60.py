from euler import primes,isPrime

def newConcatenatesPrimes(lista):
    for i in range(len(lista)-1):
        if not isPrime(int(str(lista[i])+str(lista[-1]))):
            return False
        if not isPrime(int(str(lista[-1])+str(lista[i]))):
            return False
    return True

#[3 37 67 5923 194119] suma 200149, y no funciona. Ahora buscamos listas menores
#[3, 5323, 10357, 29587, 31231] suma 76501
min=76501

prim=primes(min)

for i1 in range(len(prim)):
    for i2 in range(i1+1,len(prim)):
        if sum([prim[i1],prim[i2]*4])>min:
            break
        if newConcatenatesPrimes([prim[i1],prim[i2]]):
            for i3 in range(i2+1,len(prim)):
                if sum([prim[i1],prim[i2],prim[i3]*3])>min:
                    break
                if newConcatenatesPrimes([prim[i1],prim[i2],prim[i3]]):
                    for i4 in range(i3+1,len(prim)):
                        if sum([prim[i1],prim[i2],prim[i3],prim[i4]*2])>min:
                            break
                        if newConcatenatesPrimes([prim[i1],prim[i2],prim[i3],prim[i4]]):
                            for i5 in range(i4+1,len(prim)):
                                if sum([prim[i1],prim[i2],prim[i3],prim[i4],prim[i5]])>min:
                                    break
                                if newConcatenatesPrimes([prim[i1],prim[i2],prim[i3],prim[i4],prim[i5]]):
                                    if sum([prim[i1],prim[i2],prim[i3],prim[i4],prim[i5]])<min:
                                        print prim[i1],prim[i2],prim[i3],prim[i4],prim[i5]
                                        print min,"->",sum([prim[i1],prim[i2],prim[i3],prim[i4],prim[i5]])
                                        min=sum([prim[i1],prim[i2],prim[i3],prim[i4],prim[i5]])
                                    else:
                                        print "---",prim[i1],prim[i2],prim[i3],prim[i4],prim[i5],"---"

print "Solution: ",min

#26033
