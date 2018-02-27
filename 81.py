f = open("81.txt", "r+")
matrix = f.read().split('\n')
matrix.remove('')
for i in range(len(matrix)):
    matrix[i]=[int(x) for x in matrix[i].split(',')]


for i in range(1,len(matrix)):
    matrix[i][0]+=matrix[i-1][0]
    matrix[0][i]+=matrix[0][i-1]

for i in range(1,len(matrix)):
    for j in range(1,len(matrix)):
        if matrix[i][j-1]<matrix[i-1][j]:
            matrix[i][j]+=matrix[i][j-1]
        else:
            matrix[i][j]+=matrix[i-1][j]

print matrix[-1][-1]

#427337
