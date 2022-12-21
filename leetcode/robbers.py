class Solution:
    def rob(self, nums):
        n=len(nums)-3
        nums.append(0)
        for i in range(n,-1,-1):
            print(nums[i])
            nums[i]+=max(nums[i+3],nums[i+2])
        return max(nums[0],nums[1])
s=Solution()
print(s.rob([1,2,3,9,4]))