# -*- coding:utf-8 -*-
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

#递归实现
# class Solution:
# 	# 返回从尾部到头部的列表值序列，例如[1,2,3]
# 	def printListFromTailToHead(self, listNode):
# 		if listNode == None:
# 			return []
# 		return self.printListFromTailToHead(listNode.next)+[listNode.val]

#链表翻转
class Solution:
	# 返回从尾部到头部的列表值序列，例如[1,2,3]
	def printListFromTailToHead(self, listNode):
		cur = listNode
		pre = None
		next = None
		while cur != None:
			#找个人代替
			next = cur.next
			#让我指向上一个
			cur.next = pre
			#让上一个代替我
			pre = cur
			#我去代替下一个
			cur = next


		result = []
		while pre != None :
			result.append(pre.val)
			pre = pre.next
		return result

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4


sol = Solution()
print(sol.printListFromTailToHead(node1))