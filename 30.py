sum=0
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    for f in range(0,10):
                        if 100000*a+10000*b+1000*c+100*d+10*e+f == a**5+b**5+c**5+d**5+e**5+f**5:
                            if 100000*a+10000*b+1000*c+100*d+10*e+f>1:
                                sum+=100000*a+10000*b+1000*c+100*d+10*e+f
print sum

#443839
