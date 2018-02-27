from euler import pythagorean_triplets

dict={}

trips = [x for x in pythagorean_triplets(1000) if x[0]+x[1]+x[2]<=1000]

for t in trips:
    perim=str(t[0]+t[1]+t[2])
    if perim in dict:
        dict[perim]+=1
    else:
        dict[perim]=1


print max([(d,k) for k,d in dict.items()])

#840
