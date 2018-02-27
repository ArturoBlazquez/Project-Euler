sum=0
For[i=1,i<10000,i++,n=Total[Divisors[i]]-i;If[n≠i,If[Total[Divisors[n]]-n==i,sum+=i]]]
sum

31626
