f = open("59_in.txt", "r+")
textoCifrado = f.read().split(',')


g = open("59_out.txt", "w")

for a in range(ord('a'),ord('z')+1):
    for b in range(ord('a'),ord('z')+1):
        for c in range(ord('a'),ord('z')+1):
            key=[a,b,c]
            
            descifrado=''
            correct=True
            numSpaces=0
            for i in range(0,len(textoCifrado),3):
                try:
                    descifrado += "".join(chr(int(a) ^ b) for a, b in zip(textoCifrado[i:i+3], key))
                except ValueError:
                    correct=False
                    break
            if descifrado.count(' the ')<1:
                correct=False
            
            if correct:
                g.write(descifrado)
                break
        if correct:
            break
    if correct:
        break

print sum([ord(x) for x in descifrado])

#107359
