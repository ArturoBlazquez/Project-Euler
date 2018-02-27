def checkPandigital(num):
    if len(num)==len(set(num)) and '0' not in num:
        return True
    return False

for i in range(1,100000):
    aux=''
    for j in range(1,10):
        aux+=str(i*j)
        if len(aux)>9:
            break
        elif len(aux)==9:
            if checkPandigital(aux):
                largest=aux

print largest

#932718654
