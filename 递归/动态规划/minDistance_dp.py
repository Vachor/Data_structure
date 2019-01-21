# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 示例 1:
#
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释:
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
class Solution:
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		return self.recurs(word1,word2,len(word1),len(word2))
	def recurs(self,word1,word2, i,j):
		dp =[[0 for _ in range(j+1)] for _ in range(i+1)]
		for k in range(i+1):
			for l in range(j+1):
				if k == 0:
					dp[k][l] = l
					continue
				if l == 0:
					dp[k][l] = k
					continue

				if word1[k-1] == word2[l-1]:
					dp[k][l] = dp[k-1][l-1]
					continue
				else:
					dp[k][l] = min(dp[k-1][l-1]+1,dp[k-1][l]+1,dp[k][l-1]+1)
					continue
		return dp[i][j]