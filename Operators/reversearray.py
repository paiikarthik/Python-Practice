class Solution:
    def reverseArray(self, arr):
        n=len(arr)
        arr1=[]
        for i in range(n,0,-1):
            arr1.append(i)
        return arr1
        
        
arr=[1,2,3,4]
c=Solution()
print(c.reverseArray(arr))

class Solution:
    def reverseArray(self, arr):
        arr[:]=arr[::-1]
        return arr
        
        