class Solution(object):
    def findRestaurant(self, list1, list2):
        new=[]
        for ele in list1:
            if ele in list2:
                new.append(ele)


        min=9999999
        ans=[]

        for el in new:
            sum= list1.index(el)+list2.index(el)
            if sum<min:
                min=sum
                ans=[el]

            elif sum==min:
                ans.append(el)

        return ans
                



c=Solution()
list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
print(c.findRestaurant(list1,list2))