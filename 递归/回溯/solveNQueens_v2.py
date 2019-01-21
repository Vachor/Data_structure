class Solution:
	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		self.t = 0
		def check(cur, v):
			#如果在一列上
			if v in cur:
				return False
			#如果在对角线上
			for i, e in enumerate(cur):
				#如果前后列的差值与行的差值相同
				if abs(v - e) == len(cur) - i:
					return False
			return True

		def gen(cur):
			res = []
			for v in cur:
				res.append('.' * v + 'Q' + '.' * (len(cur) - v - 1))
			return res

		def bt(res, cur, n):
			if len(cur) == n:
				res.append(gen(cur))
			else:
				for i in range(n):
					if check(cur, i):
						cur.append(i)
						bt(res, cur, n)
						self.t += 1
						cur.pop()

		res = []
		bt(res, [], n)
		print(self.t)
		return res
print(Solution().solveNQueens(11))