# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39
# -*- coding:utf-8 -*-
import datetime
import copy

class Solution:
	def __leftExpand(self,cur,n):
		if(cur[2]==0) | (cur[2]==1):
			cur[3] = cur[2]
			cur[0] = None
			return
		cur[0] = [None,None,None,None]
		cur[0][2] = n
	def __rightExpand(self,cur,n):
		if(cur[2]==0) | (cur[2]==1):
			cur[3] = cur[2]
			cur[1] = None
			return
		cur[1] = [None,None,None,None]
		cur[1][2] = n
	def __fill_value(self,cur):
		if cur[3] != None:
			return False
		if (cur[0][3] == None) | (cur[1][3] == None):
			return False
		else:
			cur[3] = cur[0][3] + cur[1][3]
			return True
	def recurs(self,n):
		if (n==1) | (n==0):
			return n
		return self.recurs(n-1)+self.recurs(n-2)
	# def construct_tree(self, n):
	# 	# write code here
	# 	cur = TreeNode()
	# 	self.head = cur
	# 	cur.n = n
	# 	stack = []
	# 	if(cur.n != 0 & cur.n != 1):
	# 		stack.append(cur)
	# 	else:
	# 		if(cur.n == 1):
	# 			cur.value = 1
	# 		else:
	# 			cur.value = 0
	# 		return cur
	# 	while(len(stack)!=0):
	# 		while(cur != None):
	# 			cur = self.__leftExpand(cur,cur.n-1,stack)
	# 		stack.pop()
	# 		if(len(stack) != 0):
	# 			cur = stack.pop()
	# 		else:
	# 			return cur
	# 		cur = self.__rightExpand(cur,cur.n-2,stack)
	# 	return cur
	# def Fibonacci(self, n):
	# 	cur = self.head
	# 	stack = []
	# 	while(cur.value == None):
	# 		stack.append(cur)
	def construct_tree(self,n):
		self.head = [None,None,n,None]
		stack = []
		stack.append(self.head)
		while(len(stack) != 0):
			p = stack.pop()
			self.__leftExpand(p,p[2]-1)
			self.__rightExpand(p,p[2]-2)
			if(p[1] != None):
				stack.append(p[1])
			if(p[0] != None):
				stack.append(p[0])
	def fill_value(self):
		similar = []
		stack = []
		stack.append(self.head)
		while(len(stack) != 0):
			p = stack.pop()
			if(self.__fill_value(p) == False):
				similar.append(p)
			if(p[1] != None):
				stack.append(p[1])
			if(p[0] != None):
				stack.append(p[0])
		while(len(similar)!=0):
			self.__fill_value(similar.pop())
s = Solution()
start = datetime.datetime.now()
print(s.recurs(27))
end = datetime.datetime.now()
print(end-start)

start = datetime.datetime.now()
s.construct_tree(27)
s.fill_value()
end = datetime.datetime.now()
print(end-start)