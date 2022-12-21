def moveZeroes(nums) -> None:
        t=nums.count(0)
        nums=[i for i in nums if i!=0]
        try:
            while(True):nums.remove(0)
        except:pass
        nums.extend([0]*t)
        return nums
print(moveZeroes([1,23,4,0,32,0,5,24,35]))