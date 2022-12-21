def opti(days,costs):
    cost=0
    done=[]
    for i in range (0,len(days)):
        if days[i] in done: continue
        c7=0
        c30=0
        for j in range (7):
            if days[i]+j in days:
                c7+=1 
        for j in range (30):
            if days[i]+j in days:
                c30+=1
        p1=costs[0]
        p7=costs[1]/c7
        p30=costs[2]/c30
        minn=min(p1,p7,p30)
        if(p1==minn):
            cost+=costs[0]
            done.append(days[i])
            print(days[i])
            continue
        if(p7==minn):
            cost+=costs[1]
            td=[]
            for k in range(7):
                td.append(days[i]+k)
            done.extend(td)
            print(td)
            td=[]
            continue
        if(p30==minn):
            cost+=costs[2]
            td=[]
            for k in range(30):
                td.append(days[i]+k)
            done.extend(td)
            print(td)
            td=[]
            continue
    return cost

print(opti([1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28],[3,13,45]))
# print(len([1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28]))
