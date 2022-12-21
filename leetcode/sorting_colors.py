def sortColors(nums) -> None:
    dic=[0,1,1]
    for i in nums:
        dic[i]+=1
    i=-1
    for i in range (dic[0]):nums[i]=0
    for i in range (i+1,i+dic[1]):nums[i]=1
    for i in range (i+1,i+dic[2]):nums[i]=2

    print(nums)

nums = [2,0,2,2,0,2,1,1,0]
nums=[2,1,2,2,1,2]
print(sortColors(nums))
        