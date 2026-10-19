class Solution(object):
    def targetIndices(self, nums, target):
        ele=sorted(nums)
        s=[]
        for i in range(len(ele)):
            if ele[i]==target:
                s.append(i)

        return s


    
nums = [1,2,5,2,3]
target = 2
c=Solution()
print(c.targetIndices(nums,target))