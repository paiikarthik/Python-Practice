class Solution(object):
    def smallestPalindrome(self, s):
        reverse=""

        l=int(len(s)/2)
        for i in range(0,len(s)):
            left=s[0:l+1]
            left="".join(sorted(left))
            right=s[l+1:]
            right="".join(sorted(left,reverse=True))
   
        return left+right

st="babab"
c=Solution()
print(c.smallestPalindrome(st))