class Solution(object):
    
    def subsets(self, nums):
        li=[]
        for i in nums:
            li.append(i)
        return li

        
nums = [1,2,3]
c=Solution()
print(c.subsets(nums))
