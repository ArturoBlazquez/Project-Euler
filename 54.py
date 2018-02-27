HIGH_CARD = 1
PAIR = 2
TWO_PAIRS = 3
THREE = 4
STRAIGHT = 5
FLUSH = 6
FULL = 7
POKER = 8
STRAIGHT_FLUSH = 9
ROYAL_FLUSH = 10

def getNum(card):
    try:
        return int(card[0])
    except ValueError:
        if card[0]=='T':
            return 10
        if card[0]=='J':
            return 11
        if card[0]=='Q':
            return 12
        if card[0]=='K':
            return 13
        if card[0]=='A':
            return 14

def getSuite(card):
    return card[1]

def hasStraight(sortedHand):
    for i in range(0,4):
        if sortedHand[i]+1!=sortedHand[i+1]:
            return False
    return True

def getValue(disorderedHand):
    h=disorderedHand
    flush=getSuite(h[0])==getSuite(h[1]) and getSuite(h[1])==getSuite(h[2]) and getSuite(h[2])==getSuite(h[3]) and getSuite(h[3])==getSuite(h[4])
    
    hand=sorted([getNum(x) for x in disorderedHand])
    
    if flush and hasStraight(hand):
        if hand[0]==10:
            return (ROYAL_FLUSH)
        else:
            return (STRAIGHT_FLUSH, hand[4])
    
    elif hand[0]==hand[3]:
        return (POKER, hand[0], hand[4])
    elif hand[1]==hand[4]:
        return (POKER, hand[1], hand[0])
    
    elif hand[0]==hand[2] and hand[3]==hand[4]:
        return (FULL, hand[0], hand[3])
    elif hand[0]==hand[1] and hand[2]==hand[4]:
        return (FULL, hand[2], hand[0])
    
    elif flush:
        return (FLUSH, hand[4], hand[3], hand[2], hand[1], hand[0])
    
    elif hasStraight(hand):
        return (STRAIGHT, hand[4])
    
    elif hand[0]==hand[2]:
        return (THREE, hand[0], hand[4], hand[3])
    elif hand[1]==hand[3]:
        return (THREE, hand[1], hand[4], hand[0])
    elif hand[2]==hand[4]:
        return (THREE, hand[2], hand[1], hand[0])
    
    elif hand[0]==hand[1] and hand[2]==hand[3]:
        return (TWO_PAIRS, hand[2], hand[0], hand[4])
    elif hand[0]==hand[1] and hand[3]==hand[4]:
        return (TWO_PAIRS, hand[3], hand[0], hand[2])
    elif hand[1]==hand[2] and hand[3]==hand[4]:
        return (TWO_PAIRS, hand[3], hand[1], hand[0])
    
    elif hand[0]==hand[1]:
        return (PAIR, hand[0], hand[4], hand[3], hand[2])
    elif hand[1]==hand[2]:
        return (PAIR, hand[1], hand[4], hand[3], hand[0])
    elif hand[2]==hand[3]:
        return (PAIR, hand[2], hand[4], hand[1], hand[0])
    elif hand[3]==hand[4]:
        return (PAIR, hand[3], hand[2], hand[1], hand[0])
    
    else:
        return (HIGH_CARD, hand[4], hand[3], hand[2], hand[1], hand[0])


f = open("54.txt", "r+")
str = f.read()
listAux = str.split('\n')

mano=[]
for l in listAux:
    mano.append(l.split(' '))
mano.remove([''])

wins=0
for m in mano:
    first = getValue(m[0:5])
    second = getValue(m[5:10])
    
    for i in range(len(first)):
        if first[i]>second[i]:
            wins+=1
            break
        if first[i]<second[i]:
            break

print wins

#376
