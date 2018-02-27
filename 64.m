total=0;
max=10000;
For[i=0,i<=max,i++,
If[OddQ[Length[ContinuedFraction[Sqrt[i]][[2]]]],total+=1]]
total

#1322
