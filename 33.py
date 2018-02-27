from fractions import Fraction

div=Fraction(1,1)

#Get fractions ab/cb ==a/c
for a in range(1,10):
    for b in range(1,10):
        for c in range(a+1,10):
            if Fraction(10*a+b,10*c+b)==Fraction(a,c):
                div*=Fraction(10*a+b,10*c+b)

#Get fractions ab/bc == a/c
for a in range(1,10):
    for b in range(a+1,10):
        for c in range(1,10):
            if Fraction(10*a+b,10*b+c)==Fraction(a,c):
                div*=Fraction(10*a+b,10*b+c)

#Get fractions ba/bc == a/c
for b in range(1,10):
    for a in range(1,10):
        for c in range(a+1,10):
            if Fraction(10*b+a,10*b+c)==Fraction(a,c):
                div*=Fraction(10*b+a,10*b+c)

#Get fractions ba/cb == a/c
for b in range(1,10):
    for a in range(1,10):
        for c in range(b+1,10):
            if Fraction(10*b+a,10*c+b)==Fraction(a,c):
                div*=Fraction(10*b+a,10*c+b)

print div.denominator

#100
