class Solution(object):
    def reverse(self, x):
        sign=""
        if x<0:
            x=-x
            sign="-"



        sum1=""

        while x!=0:
          digit=x%10
          sum1+=str(digit)
          x=x//10

        fsum=int(sum1)

        if sign=="-":
           fsum=-fsum

        if fsum>2147483647 or fsum < -2147483648:
           return 0
        else:
           return fsum
          


c=Solution()
print(c.reverse(123))