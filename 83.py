f = open("83.txt", "r+")
matrix = f.read().split('\n')
matrix.remove('')
for i in range(len(matrix)):
    matrix[i]=[int(x) for x in matrix[i].split(',')]

def neighbours(i,j):
    m=len(matrix)-1
    ret=[]
    
    if i>0:
        ret.append((matrix[i-1][j],i-1,j))
    if j>0:
        ret.append((matrix[i][j-1],i,j-1))
    if i<m:
        ret.append((matrix[i+1][j],i+1,j))
    if j<m:
        ret.append((matrix[i][j+1],i,j+1))
    
    return ret


m=len(matrix)-1
discovered={(0,0):(m+m,matrix[0][0],m+m)}
visited=[]

#Usamos busqueda A*
while 1:
    i,j = min(discovered, key=discovered.get)
    f,g,h=discovered.pop((i,j))
    
    if i==m and j==m:
        print g
        break
    
    visited.append((i,j))
    for n in neighbours(i,j):
        if (n[1],n[2]) not in visited:
            if (n[1],n[2]) not in discovered:
                h=m-n[1]+m-n[2]
                discovered[(n[1],n[2])]=(g+n[0]+h,g+n[0],h)

#425185
