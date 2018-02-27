"""
Analizando el problema, vemos que para una cuadricula mxn, tenemos n*m piezas diferentes,
de 1x1 hay n*m
de 1x2 hay (n-1)*m
de 1x3 hay (n-2)*m, etc

de 2x1 hay n*(m-1), etc

Osea que una cuadricula nxm tendra sum(sum(i*j)) con j de m a 1 e i de n a 1=(n(n+1)/2)*(m(m+1)/2)
"""
from euler import range_infinite

def countGrid(n,m):
    return (n*(n+1)*m*(m+1))/4

#difference,n,m
nearest=(10**9,0,0)

for n in range(1,5000):
    for m in range_infinite(1):
        count=countGrid(n,m)
        if abs(2000000-count)<nearest[0]:
            nearest=(abs(2000000-count),n,m)
        elif count>2000000:
            break

print nearest
print nearest[1]*nearest[2]
