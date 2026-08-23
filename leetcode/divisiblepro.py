class Solution(object):
    def checkDivisibility(self, n):
        sum=0
        pro=1
        while n>0:
            n=n%10
            sum+=n
            pro*=n
            n=n//10

        if n%sum==0 and n%pro==0:
            return True
        return False


c=Solution()
print(c.checkDivisibility(23))