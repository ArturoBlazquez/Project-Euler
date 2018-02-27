For[i=1,i<10000000,i++,
f1=FactorInteger[i];
f2=FactorInteger[i+1];
f3=FactorInteger[i+2];
f4=FactorInteger[i+3];
ll=Join[f1,f2,f3,f4];
ls=DeleteDuplicates[ll];
If[Length[f1]>3&& Length[f2]>3 && Length[f3]>3&& Length[f4]>3 , If[Length[ll]==Length[ls],Print[i];Break[]]]
]

134043
