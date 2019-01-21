# -*- coding:utf-8 -*-
class Solution:
	def dp(self,i,n):
		dp = [0 for _ in range(n+1)]
		for j in range(n,-1,-1):
			if(j+1 == n):
				dp[j] = 1
			elif(j==n):
				dp[j] = 0
			elif(j+2 == n):
				dp[j] = 2
			else:
				dp[j] = dp[j+1]+dp[j+2]
		return dp[i]
	def recurs(self,i,n):
		if(i+1 == n):
			return 1
		if(i==n):
			return 0
		if(i+2 == n):
			return 2
		return self.recurs(i+1,n)+self.recurs(i+2,n)
	def rectCover(self, number):
		# write code here
		return self.dp(0,number)
print(Solution().rectCover(300000))