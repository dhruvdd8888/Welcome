def maxSatisfaction(satisfaction):
    satisfaction.sort()
    if(satisfaction[-1]<=0):return 0
    sums=[]
    for j in range (len(satisfaction)):
        ss=satisfaction[j:]
        sums.append(sum([(i+1)*ss[i] for i in range(0,len(ss))]))
    return max(sums)

print(maxSatisfaction([3,2,4]))