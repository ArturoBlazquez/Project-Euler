#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Hay 3 posibles diagonales,
d1=sqrt(a²+(b+c)²)
d2=sqrt(b²+(a+c)²)
d3=sqrt(c²+(a+b)²)

Pero sólo nos interesa si d1 es la diagonal más pequeña, es decir, d1<d2 y d1<d3
d1<=d2 <=> b<=a
d1<=d3 <=> c<=a

Fijamos a, que lo cojemos de una terna, b+c=p[1], y conseguimos el rango de b, sabiendo b<=a, c<=a, c=p[1]-b
p[1]-a<=b<=a

También b>0, que lo tenemos gracias a que las ternas están ordenadas y c>0 => b<=p[1]

Además no queremos cuboides repetidos, así que b<=c => b>=p[1]/2
"""

from euler import pythagorean_triplets,range_infinite
import itertools
from math import sqrt

for n in range_infinite(1800):
    trips1=[(x[0],x[1],x[2]) for x in pythagorean_triplets(n*10) if x[0]<=n and x[1]<=2*n]
    trips2=[(x[1],x[0],x[2]) for x in pythagorean_triplets(n*10) if x[1]<=n and x[0]<=2*n]

    trips=trips1+trips2

    tot=0    
    for p in trips:
        a=p[0]
        tot+=len(range(max(p[1]-a,int((p[1]+1)/2)),min(a+1,p[1])))
    
    print n, tot
    if tot>10**6:
        print n
        break

#1818
