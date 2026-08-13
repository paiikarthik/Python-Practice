class Solution(object):
    def isPowerOfFour(self, n):
        for i in range(0,1000):
            if pow(4,i)==n:
                return True
            
        return False


c=Solution()
print(c.isPowerOfFour(213009))
