from euler import range_infinite

cubes=[]

for i in range_infinite():
    cubes.append(sorted(str(i**3)))
    if cubes.count(sorted(str(i**3)))==5:
        break

for i in range_infinite():
    if cubes.count(sorted(str(i**3)))>=5:
        print i**3
        break

#127035954683
