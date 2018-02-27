from euler import get_digit

chain={1:1,89:89}

for i in range(2,10**7+1):
    if i not in chain:
        this=i
        actualChain=[this]
        while 1:
            next=0
            for j in range(len(str(this))):
                next+=get_digit(this,j)**2
            
            if next in chain:
                chain[this]=chain[next]
                break
            else:
                this=next
                actualChain+=[this]
        
        for a in actualChain:
            chain[a]=chain[this]

print len([x for x in chain.values() if x==89])
