class Solution(object):
    def largestInteger(self, n, s):
        if s>9*n: # if s>9 [19>9*2]
            return -1
            
        ans=""
        
        for i in range(n):
            digit=min(9,s) #find minimum among lar num and s 
            ans+=str(digit) #add to answer
            s-=digit #subtract from s to get remaining digit
        return int(ans)

