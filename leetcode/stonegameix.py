class Solution(object):
    def stoneGameIX(self, stones):
        if len(stones)==1:
            return False
        sum=0

        for i in range(len(stones)):
            sum+=stones[i]

        if sum%3==0:
            return True

stones = [5,1,2,4,3]
c=Solution()
print(c.stoneGameIX(stones))