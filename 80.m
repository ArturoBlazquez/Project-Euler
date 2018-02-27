tot=0;
For[i=0,i<100,i++,If[Total[RealDigits[Sqrt[i],10,100][[1]]]!=Sqrt[i],tot+=Total[RealDigits[Sqrt[i],10,100][[1]]]]]
tot

(* 40886 *)
