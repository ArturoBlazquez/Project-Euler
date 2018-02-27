from sets import Set

list=Set()

for a in range(2,101):
    for b in range(2,101):
        list.add(a**b)

print len(list)

#9183
