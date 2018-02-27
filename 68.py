def range_excluded(ini,end,excluded):
    ret=range(ini,end)
    for i in excluded:
        ret.remove(i)
    return ret

def incr(index):
    if index==4:
        return 0
    else:
        return index+1

sols=[]
for n in range(9,21):
    for x1 in range(1,11):
        for x2 in range_excluded(1,11,[x1]):
            for x4 in range_excluded(1,11,[x1,x2]):
                for x5 in range_excluded(1,11,[x1,x2,x4]):
                    for x6 in range_excluded(1,11,[x1,x2,x4,x5]):
                        x3=n-x1-x2
                        x7=n-x3-x4
                        x8=n-x4-x5
                        x9=n-x5-x6
                        x10=n-x6-x2
                        s=set([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10])
                        
                        if len(s)==10 and sum(s)==55 and max(s)==10 and min(s)==1:
                            sol=[[x1,x2,x3],[x7,x3,x4],[x8,x4,x5],[x9,x5,x6],[x10,x6,x2]]
                            
                            index=sol.index(min(sol))
                            string=''
                            for i in range(5):
                                string+=str(sol[index][0])+str(sol[index][1])+str(sol[index][2])
                                index=incr(index)
                            
                            print n," -> ", string
                            if len(string)==16:
                                sols.append(int(string))
print max(sols)

#6531031914842725
