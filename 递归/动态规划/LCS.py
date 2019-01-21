def LCS_recurs(i,j,a,b):
	if(i==-1) | (j==-1):
		return 0

	if(a[i] == b[j]):
		return LCS_recurs(i-1,j-1,a,b)+1
	else:
		return max(LCS_recurs(i-1,j,a,b),LCS_recurs(i,j-1,a,b))
def LCS_dp(i,j,a,b):
	dp = [[0 for _ in range(j+2)] for _ in range(i+2)]   #动态规划表的下标只能从0开始, 如果从-1开始的话, 那么d[i][j]就是a[0..i],和b[0..j]的最大公共子序列
	for r in range(i+2):                                     #但是这个表是从0开始的, 那么d[i][j]代表的是a[0...i-1]和b[0..j-1]的最大公共子序列
		for c in range(j+2):
			if(r==0) | (c==0):
				dp[r][c] = 0
			else:
				if(a[r-1] == b[c-1]):
					dp[r][c] = dp[r-1][c-1]+1
				else:
					dp[r][c] = max(dp[r-1][c],dp[r][c-1])
	return dp[i+1][j+1]
a = ['A','B','C','D','G']
b = ['B','C','D']
print(LCS_recurs(4,2,a,b))
print(LCS_dp(4,2,a,b))