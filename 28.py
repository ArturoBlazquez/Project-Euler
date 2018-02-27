def upRight(n):
    return sum([x*x for x in range(3,n*2+3,2)])

def upLeft(n):
    return sum([x*x+x+1 for x in range(2,n*2+2,2)])

def downRight(n):
    return sum([x*x+x+1 for x in range(1,n*2+1,2)])

def downLeft(n):
    return sum([x*x+1 for x in range(2,n*2+2,2)])

n=500
print upRight(n)+upLeft(n)+downRight(n)+downLeft(n)+1

#669171001
