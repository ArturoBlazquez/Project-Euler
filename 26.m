max=0;
num=0;
For[i=2,i<1000,i++,n=Length[Last[First[RealDigits[1/i]]]];If[n>max,max=n;num=i]]
num

983
