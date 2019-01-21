# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
class Solution:
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		self.res = []
		self.n = n
		self.k = k
		#第一阶段的所有决策, 参数:组合,当前列,上一个列的选择
		self.recurs([],1,0)
		return self.res
	def recurs(self,nums,cur,pre):
		if cur == self.k+1:
			self.res.append(nums.copy())
			return

		#决策: 比如上一列的选择是1那么这个列的选择就是2,3,4..., 如果上一列的选择是2那么这列就是3,4,5...
		for i in range(pre+1,self.n+1):
			nums.append(i)
			self.recurs(nums,cur+1,i)
			nums.pop()
		return self.res