class Solution(object):

    def lengthOfLIS(self, nums):
        current=1
        longest=1

        start=0
        new=0
        end=0
        for i in range(1,len(nums)-1):
            if nums[i+1]>nums[i]:
                current+=1
            else:
               current=1
               start=i

            if current>longest:
                longest=current
                new=start
                end=i

        res= nums[new:end+1]
        return res


nums = [10,9,2,5,3,7,101,18]
c=Solution()
print(c.lengthOfLIS(nums))