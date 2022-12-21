def twoSum(nums, target):
    n=len(nums)
    for i in range (n):
        toFind=target-[nums[i]]
        if toFind in nums:
            return [nums[i],toFind]

l=[1,2,3]
print(l.index(3))