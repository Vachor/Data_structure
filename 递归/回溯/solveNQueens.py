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
		#初始化棋盘
		check = [['.' for _ in range(n)] for _ in range(n)]
		#递归
		for k in range(1,n+1):
			self.recurs_setQueen(copy.deepcopy(check),n,1,k)
		return self.out
	def setQueen(self,check,rows,i):
		#在rows行,i列设置皇后
		check[rows-1][i-1] = 'Q'
	def isLegal(self,check,rows,i):
		#检查一列有没有皇后
		r = rows-2
		c = i-1
		while not (r == -1):
			if check[r][c] == 'Q':
				return False
			r -= 1
		#检查对角线
		r = rows-2
		c = i-2
		while not ((r==-1) | (c == -1)):
			if check[r][c] == 'Q':
				return False
			r -= 1
			c -= 1
		r = rows-2
		c = i
		while not ((r==-1) | (c == self.n)):
			if check[r][c] == 'Q':
				return False
			r -= 1
			c += 1
		return True
	def display(self,check):
		list = []
		for i in check:
			list.append(''.join(i))
		self.out.append(list)
	def recurs_setQueen(self,check,n,rows,cols):
		self.setQueen(check,rows, cols)
		if self.isLegal(check,rows, cols) == False:
			return

		if rows == n:
			self.display(check)
			return
		for i in range(1,n+1):
			self.recurs_setQueen(copy.deepcopy(check),n,rows+1,i)