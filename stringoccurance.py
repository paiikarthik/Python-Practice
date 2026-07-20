class Solution(object):
    def strStr(self, haystack, needle):
            if needle in haystack:
                return haystack.index(needle)
            else:
                return -1
            

            
haystack = "sosaaddsaadbutsaadbutsad"
needle = "sad"           
c=Solution()
print(c.strStr(haystack,needle))