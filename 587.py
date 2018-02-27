#Reduce[(x-r)^2+(y-r)^2==r^2&&x≤r&&y≤r&&y==x/n&&x>0&&y>0&&r==1>0&&n>0,{x,y}]

from math import sqrt, acos, pi

for n in range(1,3000):
	x=-sqrt(2.0)*sqrt(n**3/(1.0+n*n)**2)+(n+n*n)/(1.0+n*n)
	y=x/n
	t=acos(1-y)
	percentage = ((1-n*t+(n-1)*(1-x))*200)/(n*(4-pi))
	if percentage<0.1:
		print n
		break

#2240
