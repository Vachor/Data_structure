#位运算解8皇后问题
class Solution(object):
	def totalNQueens(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n < 1: return []
		self.count = 0
		self.DFS(n, 0, 0, 0, 0)
		return self.count

	def DFS(self, n, row, col, pie, na):

		if row >= n:
			self.count += 1
			return

		bits = (~(col | pie | na)) & ((1 << n) - 1)

		while bits:
			p = bits & -bits
			self.DFS(n, row + 1, col + p, (pie | p) << 1, (na | p) >> 1)
			bits = bits & (bits - 1)
print(Solution().totalNQueens(4))