#一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
# -*- coding:utf-8 -*-
import datetime
class Solution:
	def jumptimes_recurs(self,number,i):
		if (i==number):
			return 0
		if (i==number-1):
			return 1
		if (i==number-2):
			return 2
		return self.jumptimes_recurs(number,i+1)+self.jumptimes_recurs(number,i+2)
	def jumptimes_dp(self,number,i):
		dp = [0 for _ in range(number+1)]
		for m in range(number,-1,-1):
			if(m==number):
				dp[m] = 0
			elif(m==number-1):
				dp[m] = 1
			elif(m==number-2):
				dp[m] = 2
			else:
				dp[m]=dp[m+1]+dp[m+2]
		return dp[i]
	def jumpFloor(self, number):
		return self.jumptimes_dp(number,0)

start = datetime.datetime.now()
for i in range(34):
	print(Solution().jumptimes_dp(i,0),end=' ')
end = datetime.datetime.now()
print(end-start)

start = datetime.datetime.now()
for i in range(34):
	print(Solution().jumptimes_recurs(i,0),end=' ')
end = datetime.datetime.now()
print(end-start)
