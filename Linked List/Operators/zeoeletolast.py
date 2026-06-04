class Solution:
	def pushZerosToEnd(self, arr):
		new=[]
		zero=0
		for ele in arr:
			if ele!=0:
				new.append(ele)
			else:
				zero+=1
		return new +[0]*zero


arr=[3,5,0,0,4]
c=Solution()
print(c.pushZerosToEnd(arr))
