#给定一个整数 n，返回 n 皇后不同的解决方案的数量。

# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
import copy

class Solution:
	def totalNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		self.out = []
		self.n = n
		#初始化棋盘
		check = []
		#递归
		sum = 0
		for k in range(n):
			sum += self.recurs_getNOQueen(check,k)
		return sum
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
	def recurs_getNOQueen(self,check,cols):
		sum = 0
		check.append(cols)
		if self.isLegal(check) == False:
			check.pop()
			return 0
		if len(check) == self.n:
			check.pop()
			return 1


		for i in range(self.n):
			sum += self.recurs_getNOQueen(check,i)
		check.pop()
		return sum