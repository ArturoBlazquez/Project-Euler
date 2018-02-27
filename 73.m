total=0;
For[d=12000,d>1,d--,
If[EvenQ[d],top=d/2-1,top=IntegerPart[d/2]];
For[n=IntegerPart[d/3]+1,n<=top,n++,
If[GCD[n,d]==1,total+=1]]]
total

(* 7295372 *)
