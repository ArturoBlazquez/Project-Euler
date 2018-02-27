max=0;
maxd=0;
For[d=0,d<=1000,d++,
num=Min[Solve[x^2 - d y^2 == 1 &&y>0&&10^55>=x>0, {x,y}, Integers]][[1,2]];
If[num>max,max=num;maxd=d]]
max
maxd

661
