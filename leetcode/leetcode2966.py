class Solution(object):

    def missingInteger(self, nums):
        new=[]
        for i in range(0,len(nums)):
                if nums[i]+1==nums[j]:
                    new.append(nums[j])

        return new

        


nums=[1,2,3,2,5]
c=Solution()
print(c.missingInteger(nums))