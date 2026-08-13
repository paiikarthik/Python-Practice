class Solution(object):
    def lengthOfLongestSubstring(self, s):
       new=set()

       left=0
       res=0

       for i in range(len(s)):
           while s[i] in new:
               new.remove(s[left])
               left+=1
           new.add(s[i])

           res=max(res,i - left+1) 
       return res
               

s="abcabcde"

b=Solution()
print(b.lengthOfLongestSubstring(s))