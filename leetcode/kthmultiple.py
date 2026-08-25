class Solution(object):
    def missingMultiple(self, nums, k):
     
        for i in range(1,len(nums)+1):
          ele=i*k
          if ele not in nums:
             return ele

       



nums = [8,2,3,4,6]
k = 2
        
c=Solution()
print(c.missingMultiple(nums,k))