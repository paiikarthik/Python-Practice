class Solution:
    def singleNonDuplicate(self,arr):
        l=len(arr)
        new=[]
        count=0
        for i in range(0,l-2):
            for j in range(0,l-1):
                if (arr[i]!=arr[j]):
                    count+=1

            if count==1:
                new.append(arr[i])
        return new


arr= [1,1,2,2,4,5,5]
c=Solution()
print(c.singleNonDuplicate(arr))
