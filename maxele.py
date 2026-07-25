class Solution(object):
    def maxProduct(self, n):
       new=[]
       while n > 0:
         new.append(n % 10)
         n //= 10
       new.sort()
       set(new)
       max=new[0]
       min=new[0]
       for i in range(1,len(new)):
          
          if new[i]>max:
             min=max
             max=new[i]

  
       return min*max

s=767
c=Solution()
print(c.maxProduct(s))
           
        
        