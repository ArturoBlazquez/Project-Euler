#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
top=50

grid=[(x,y) for x in range(top+1) for y in range(top+1)]
grid.remove((0,0))

all=[]
for i in grid:
    for j in grid:
        a=i[0]
        b=i[1]
        c=j[0]
        d=j[1]
        
        l1=a*a+b*b
        l2=c*c+d*d
        l3=(c-a)**2+(d-b)**2
        
        if 2*max(l1,l2,l3)==sum([l1,l2,l3]):
            if i!=j:
                if a>c:
                    all.append((j,i))
                elif c>a:
                    all.append((i,j))
                else:
                    if b>d:
                        all.append((j,i))
                    else:
                        all.append((i,j))

print len(set(all))"""

from fractions import Fraction

max=50
total=0

#Primero vemos los que hacen ángulo recto en el origen, los dos puntos están en el eje de coordenadas
total+=max*max

#Ahora los que tienen los dos puntos en la misma vertical o en la misma horizontal
total+=max*max*2

#Y por último los que hacen ángulos rectos en otras partes
grid=[(x,y) for x in range(1,max+1) for y in range(1,max+1)]

for p in grid:
    #Vemos hacia arriba
    n=Fraction(p[0],p[1]).numerator
    d=Fraction(p[0],p[1]).denominator
    q=(p[0]-d,p[1]+n)
    while q[0]>=0 and q[1]<=max:
        total+=1
        q=(q[0]-d,q[1]+n)
    
    #Vemos hacia abajo
    q=(p[0]+d,p[1]-n)
    while q[0]<=max and q[1]>=0:
        total+=1
        q=(q[0]+d,q[1]-n)

print total

#14234
