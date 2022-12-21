def searchRange( nums, target: int):
    s=0
    l=len(nums)-1
    e=l
    first=-1
    last=-1
    while(s<=e):
        m=int((s+e)/2)
        if(nums[m]==target and (m==0 or nums[m-1]!=target )):
            first=m
            break
        elif(nums[m]>=target):
            e=m-1
        else:
            s=m+1
    s=0
    l=len(nums)-1
    e=l
    while(s<=e):
        m=int((s+e)/2)
        print(s,m,e)
        if(nums[m]==target and (m==e or nums[m+1]!=target )):
            last=m
            break
        elif(nums[m]<=target):
            s=m+1
        else:
            e=m-1
            
    return (first,last)



print(searchRange([1,3,3,3,4,5],2))
