class Solution(object):
   
    def generate(self, numRows):
        li=[]
        num=1
        for i in range(numRows):
           li.append([num])
        return li
           

numRows = 5
c=Solution()
print(c.generate(numRows))