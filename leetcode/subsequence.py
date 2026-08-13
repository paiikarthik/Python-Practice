class Solution(object):
    def maxProduct(self, nums):
        
        curr=1
        longest=1

        start=0
        newstart=0
        end=0

        for i in range(1,len(nums)):

            if nums[i]==nums[i-1]+1:
                curr+=1
            else:
                curr=1
                start=i

            
            if curr>longest:
                longest=curr
                newstart=start
                end=i

            res=nums[newstart:end+1]

        sum=1
        for i in res:
            sum*=i

        return sum


ele=[-2,0,-1]
c=Solution()
print(c.maxProduct(ele))
