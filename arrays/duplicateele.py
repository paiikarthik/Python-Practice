class Solution(object):
    def numOfStrings(self, patterns, word):
        count=0
        for i in range(len(patterns)):
            if word[i] in patterns[i]:
                count+=1
            return count
        

c=Solution()
patterns = ["a","abc","bc","d"]
word = "abc"
print(c.numOfStrings(patterns,word))
        