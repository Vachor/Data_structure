# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
import copy

class Solution:
	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		self.out = []
		self.n = n
		self.t = 0
		#初始化棋盘
		check = []
		#递归
		for k in range(n):
			self.recurs_setQueen(check,k)
		print(self.t)
		return self.out
	def isLegal(self,check):
		#检查一列有没有皇后
		pos = len(check)-1
		if check[pos] in check[:pos]:
			return False
		#检查对角线
		for i in range(pos-1,-1,-1):
			if abs(check[i]-check[pos]) == pos - i:
				return False
		return True
	def display(self,check):
		list = []
		for i in check:
			list.append('.'*i + 'Q'+'.'*(self.n-i-1))
		self.out.append(list)
	def recurs_setQueen(self,check,cols):
		check.append(cols)
		if self.isLegal(check) == False:
			check.pop()
			return
		if len(check) == self.n:
			self.display(check)
			check.pop()
			return
		for i in range(self.n):
			self.recurs_setQueen(check,i)
			self.t += 1
		check.pop()
print(Solution().solveNQueens(11))