coins=[200,100,50,20,10,5,2]
max=200
total=0

def getCombinations(position, sum):
    global total
    if position==len(coins):
        total+=1
        return
    
    for i in range(sum/coins[position],-1,-1):
        if i*coins[position]==sum:
            total+=1
        else:
            getCombinations(position+1, sum-i*coins[position])


getCombinations(0,max)
print total

#73682
