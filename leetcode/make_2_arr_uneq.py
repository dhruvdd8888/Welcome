

def minimumTotalCost(nums1, nums2) -> int:
    # def swap(nums1,i,j):
        # nums1[i],nums1[j]=nums1[j],nums1[i]
    n=len(nums1)
    toswap=[]
    ts=[]
    tts=[]
    cost=0
    t=0
    for i in range(n):
        if(nums1[i]!=nums2[i]):continue
        else:
            ts.append(i)
            t+=1
        if(t==2):
            # print(ts)
            if(nums1[ts[0]]==nums1[ts[1]]):
                tts.append(ts[1])
                ts=ts[:-1]
            # toswap.append(ts)
            else:
                print(ts)
                t=0    
                cost=cost+ts[0]+ts[1]
                ts=[]
    tts.extend(ts)
    for i in range(len(tts)):
        if(nums1[tts[i]]!=nums2[i]):cost=cost+i+tts[i]
        else: return -1
    # print(toswap)
    # for i in toswap:
    #     cost+=i[0]+i[1]
    #     print(i)
    #     # swap(nums1,i[0],i[1])
    return cost

nums1 = [2,2,2,1,3]
nums2=[1,2,2,3,3]
# swap(nums1,1,3)
print(nums1)
print(minimumTotalCost(nums1,nums2))