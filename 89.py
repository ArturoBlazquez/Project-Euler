from euler import validRomanToInt,intToRoman

f = open("89.txt", "r+")
romans = f.read().split('\n')

saved=0
for r in romans:
    saved+=len(r)-len(intToRoman(validRomanToInt(r)))

print saved

#743
