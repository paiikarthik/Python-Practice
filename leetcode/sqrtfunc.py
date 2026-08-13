class Solution(object):
    def mySqrt(self, x):
        ele=0
        i=1
        while (i*i<=x):
            ele=i
            i+=1
        return ele
            
                 

x=10
c=Solution()
print(c.mySqrt(x))