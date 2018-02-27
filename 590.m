factor=FactorInteger[Apply[LCM, Range[5]]]
numDivisors=Product[factor[[i,2]]+1,{i,1,Length[factor]}]
pow1=numDivisors-1
pow2=numDivisors-1-Length[factor]
hl50000=PowerMod[2,pow1,10^9]+PowerMod[2,pow2,10^9]
Mod[hl50000,10^9]




list=Subsets[{1,2,3,4,5,6,10,12,15,20,30,60}];
Delete[list,1]
Length[Select[list,Apply[LCM,#]==60&]]


