def LCS_recurs(i,j,a,b):
	if(i==-1) | (j==-1):
		return 0

	if(a[i] == b[j]):
		return LCS_recurs(i-1,j-1,a,b)+1
	else:
		return max(LCS_recurs(i-1,j,a,b),LCS_recurs(i,j-1,a,b))
def LCS_dp(i,j,a,b):
	dp = [[0 for _ in range(j+1)] for _ in range(i+1)]
	for k in range(i+1):
		for l in range(j+1):

			dp[3][0] = dp[2][0]
			if (a[k] == b[l]):
				if (k-1 == -1) | (l-1 == -1):
					dp[k][l] = 0 + 1
				else:
					dp[k][l] = dp[k - 1][l - 1] + 1
				continue
			else:
				if (k-1 == -1) & (l-1 == -1):
					dp[k][l] = 0
				elif (l-1 == -1):
					dp[k][l] = dp[k-1][l]
				elif (k-1 == -1):
					dp[k][l] = dp[k][l - 1]
				else:
					dp[k][l] = max(dp[k - 1][l],dp[k][l - 1])

	return dp[i][j]
a = ['A','B','C','D','G']
b = ['B','C','D']
print(LCS_recurs(4,2,a,b))
print(LCS_dp(4,2,a,b))