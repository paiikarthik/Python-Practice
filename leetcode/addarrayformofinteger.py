class Solution(object):
    def addToArrayForm(self, num, k):
        sum=0
        digit=""
        for ele in num:
            digit+=str(ele)

        sum=int(digit)+k
        st=[]

        while sum!=0:
            dig=sum%10
            st.append(dig)
            sum=sum//10

        return st[::-1]
            


        
num = [1,2,0,0]
k = 34
c=Solution()
print(c.addToArrayForm(num,k))