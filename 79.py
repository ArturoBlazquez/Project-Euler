#Suponemos que no hay digitos repetidos

f = open("79.txt", "r+")
keys = f.read().split('\n')
keys.remove('')

digits=[int(x) for x in sorted(set(''.join(keys)))]
key_len=len(digits)

key={}
for d in digits:
    key[d]=0


for k in keys:
    d0=int(k[0])
    d1=int(k[1])
    d2=int(k[2])
    if key[d1]<key[d0]+1:
        key[d1]=key[d0]+1
    if key[d2]<key[d1]+1:
        key[d2]=key[d1]+1

print ''.join([str(x) for x,y in sorted(key.items(), key=lambda x: x[1])])
