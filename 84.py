from random import shuffle,randint

def toStr(num):
    if num>9:
        return str(num)
    else:
        return '0'+str(num)

def rollDice():
    d1=randint(1,4)
    d2=randint(1,4)
    return d1+d2,d1==d2

def pickCard(pile,position):
    card=pile.pop(0)
    try:
        card+1
    except TypeError:
        if card=="Go":
            position=posGo
        elif card=="Jail":
            position=posJail
        elif card=="C1":
            position=posC1
        elif card=="E3":
            position=posE3
        elif card=="H2":
            position=posH2
        elif card=="R1":
            position=posR1
        elif card=="R":
            position=nextR(position)
        elif card=="U":
            position=nextU(position)
        elif card=="-3":
            position-=3
    pile.append(card)
    return position

def nextR(position):
    if position<posR1:
        return posR1
    elif position<posR2:
        return posR2
    elif position<posR3:
        return posR3
    elif position<posR4:
        return posR4
    else:
        return posR1

def nextU(position):
    if position<posU1:
        return posU1
    elif position<posU2:
        return posU2
    else:
        return posU1


ComunityChest=["Go","Jail",3,4,5,6,7,8,9,10,11,12,13,14,15,16]

Chance=["Go","Jail","C1","E3","H2","R1","R","R","U","-3",11,12,13,14,15,16]

Board=["Go","A1","CC1","A2","T1","R1","B1","CH1","B2","B3",
       "Jail","C1","U1","C2","C3","R2","D1","CC2","D2","D3",
       "FP","E1","CH2","E2","E3","R3","F1","F2","U2","F3",
       "G2J","G1","G2","CC3","G3","R4","CH3","H1","T2","H2"]

BoardDict={Board.index(key):0 for key in Board}

posGo=Board.index("Go")
posJail=Board.index("Jail")

posR1=Board.index("R1")
posR2=Board.index("R2")
posR3=Board.index("R3")
posR4=Board.index("R4")

posU1=Board.index("U1")
posU2=Board.index("U2")

posC1=Board.index("C1")
posE3=Board.index("E3")
posH2=Board.index("H2")

for game in range(100):
    shuffle(ComunityChest)
    shuffle(Chance)
    position=0
    numDoubles=0

    for _ in range(100000):
        roll,double=rollDice()

        if double:
            numDoubles+=1
        else:
            numDoubles=0

        if numDoubles>=3:
            numDoubles=0
            position=posJail
        else:
            position+=roll
            if position>39:
                position-=40
            
            if Board[position]=="G2J":
                position=posJail
            elif Board[position][:2]=="CH":
                position=pickCard(Chance,position)
            elif Board[position][:2]=="CC":
                position=pickCard(ComunityChest,position)
        
        BoardDict[position]+=1
    if game%10==0:
        print game, "games"

ordered=sorted(BoardDict, key=BoardDict.get, reverse=True)

print toStr(ordered[0])+toStr(ordered[1])+toStr(ordered[2])

#101524
