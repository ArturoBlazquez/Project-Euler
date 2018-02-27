left=0;
For[d=1000000,d>1,d--,
For[n=IntegerPart[d/2]+1,n>0,n--,
If[n/d<3/7&&n/d>left,left=n/d];
If[n/d<left,Break[]]]]
left

(* 428570 *)
