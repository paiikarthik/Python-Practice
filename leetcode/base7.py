class Solution(object):
    def convertToBase7(self, num):
       res=""
       rem=0
       sign=" "
       if num==0: #if num is zero return  it
          return 0


       if num<0:  #if number is neg then sign = -
          sign = "-"
          num=-num #& -ve number becomes positive

       while num!=0:
          rem=num%7
          res+=str(rem)
          num=num//7
       return sign + res[::-1] 
       
         

c=Solution()
print(c.convertToBase7(999))