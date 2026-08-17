class Solution(object):
    def addDigits(self, num):
        sum=0
        while num!=0:
            sum+=num%10
            num=num//10

        final=0
        while sum!=0:
            final+=sum%10
            sum=sum//10

        return final

         


num=9999
c=Solution()
print(c.addDigits(num))