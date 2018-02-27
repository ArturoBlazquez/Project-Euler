from math import factorial

tot=1000000
nums=range(0,10)
res=[]

sum=0
pos=0
for i in range(9,0,-1):
    while 1:
        sum+=factorial(i)
        if sum>=tot:
            sum-=factorial(i)
            res.append(nums[pos])
            nums.remove(nums[pos])
            pos=0
            break
        pos+=1

res.append(nums[0])

print("".join(str(x) for x in res))

#2783915460
