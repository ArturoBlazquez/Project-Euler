import numpy

f = open("82.txt", "r+")
matrix = f.read().split('\n')
matrix.remove('')
for i in range(len(matrix)):
    matrix[i]=[int(x) for x in matrix[i].split(',')]


matrix=numpy.array(matrix)

for i in range(1,len(matrix)):
    matAux=[]
    for j in range(len(matrix)):
        aux=[]
        for k in range(len(matrix)):
            if k<=j:
                aux.append(matrix[k][i-1]+sum(matrix[k:j:,i]))
            else:
                aux.append(matrix[k][i-1]+sum(matrix[j+1:k+1:,i]))
        matAux.append(matrix[j][i]+min(aux))
    matrix[:,i]=matAux

print min([x[-1] for x in matrix])

#260324
