class Solution(object):
    def sumDecoded(self, nums):
       for i in range(len(nums)):
           width=nums[i]%10
           d=nums[i]//10
           return  d

       
nums = [231]
c=Solution()
print(c.sumDecoded(nums))