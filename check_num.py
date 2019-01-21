# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# -*- coding:utf-8 -*-
class Solution:
	# array 二维列表
	def Find(self, target, array):
		if (len(array) == 0) | (len(array[0]) == 0):
			return False
		i,j = 0,len(array[0])-1
		while (array[i][j] != target):
			if array[i][j] > target:
				j -= 1
			elif array[i][j] < target:
				i += 1
			if not ((j>=0) & (i<len(array))):
				return False
		return True

a = [[]]
print(len(a) == 0)
sol = Solution()
array = [[1,2,3,4,5],[3,4,5,6,7],[5,6,7,8,9]]
print(sol.Find(-5,array))
