class Solution(object):
    
    def maxTotalValue(self, value, decay, m):
        sum=0
        i=0
        n=len(value)
        while(i<m):
            index = i % len(value)
            if(i<n):
              sum+=value[index]
              
            else:
                sum+=value[index]-decay[index]
            i+=1
        return sum
        

value = [4,3]
decay = [5,4]
m = 5

c=Solution()
print(c.maxTotalValue(value,decay,m))

        