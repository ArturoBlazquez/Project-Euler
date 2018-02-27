f = open("22.txt", "r+")
str = f.read()

list = str.split(',')

total=0
pos=1
for i in sorted(list):
    score=0
    for j in i:
        if ord(j)>=64 and ord(j)<=90:
            score=score+ord(j)-64
    score*=pos
    pos+=1
    total+=score

print total

f.close()

#871198282
