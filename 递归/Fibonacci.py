# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39
# -*- coding:utf-8 -*-
import datetime
import copy
class TreeNode:
	def __init__(self,n=None,value=None,left=None,right=None):
		self.n = n
		self.value = value
		self.left = left
		self.right = right
class Solution:
	def __leftExpand(self,cur,n):
		if(cur.n==0) | (cur.n==1):
			cur.value = cur.n
			cur.left = None
			return
		cur.left = TreeNode()
		cur.left.n = n
	def __rightExpand(self,cur,n):
		if(cur.n==0) | (cur.n==1):
			cur.value = cur.n
			cur.right = None
			return
		cur.right = TreeNode()
		cur.right.n = n
	def __fill_value(self,cur):
		if cur.value != None:
			return False
		if (cur.left.value == None) | (cur.right.value == None):
			return False
		else:
			cur.value = cur.left.value + cur.right.value
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
		self.head = TreeNode(n)
		stack = []
		stack.append(self.head)
		while(len(stack) != 0):
			p = stack.pop()
			self.__leftExpand(p,p.n-1)
			self.__rightExpand(p,p.n-2)
			if(p.right != None):
				stack.append(p.right)
			if(p.left != None):
				stack.append(p.left)
	def fill_value(self):
		similar = []
		stack = []
		stack.append(self.head)
		while(len(stack) != 0):
			p = stack.pop()
			if(self.__fill_value(p) == False):
				similar.append(p)
			if(p.right != None):
				stack.append(p.right)
			if(p.left != None):
				stack.append(p.left)
		while(len(similar)!=0):
			self.__fill_value(similar.pop())
s = Solution()
start = datetime.datetime.now()
print(s.recurs(26))
end = datetime.datetime.now()
print(end-start)
start = datetime.datetime.now()
s.construct_tree(26)
s.fill_value()
print(s.head.value,end=' ')
end = datetime.datetime.now()
print(end-start)