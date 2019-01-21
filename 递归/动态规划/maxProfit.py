class Solution:
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		self.prices = prices
		return self.recurs(len(prices))
	def recurs(self,n_cur):
		dp = [0 for _ in range(n_cur+1)]

		for i in range(n_cur+1):
			if i == 1:
				dp[i] = 0
				continue
			if i == 0:
				dp[i] = 0
				continue
			#状态转移: 当前的i天出售的最大获益等于max(0..i-1的最大获益,第i天的最大获益)
			dp[i] = max(dp[i-1],self.prices[i-1]-min(self.prices[:i-1]))
		return dp[n_cur]
	# def dp(self,cur):
	# 	if cur <= 0:
	# 		return 0
	#
	# 	a = self.recurs(cur-1)
	# 	b = self.prices[cur]-min(self.prices[:cur])
	# 	return max(a,b)