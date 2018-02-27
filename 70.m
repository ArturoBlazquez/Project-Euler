(*Empezamos por min=21, seguimos con 1514419, etc. Vamos guardando hasta que n llegamos y continuamos de ahí porque no da wolfram para hacerlo de una*)
min=8319823;
maxn=0;
For[n=8856748,n<10^7,n++,If[Sort[IntegerDigits[EulerPhi[n]]]==Sort[IntegerDigits[n]]&&n/EulerPhi[n]<min/EulerPhi[min],min=n];maxn=n]
min
maxn

(* 8319823 *)
