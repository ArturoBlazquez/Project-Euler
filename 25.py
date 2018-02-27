fib0=1
fib1=1

pos=3
while 1:
    aux=fib1
    fib1+=fib0
    fib0=aux
    if len(str(fib1))>=1000:
        break
    pos+=1

print pos

#4782
