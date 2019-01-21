# Definition for a undirected graph node
class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution:
	# @param node, a undirected graph node
	# @return a undirected graph node
	def cloneGraph(self, node):
		map = {}
		#递归得到的值是map中key为node的value, 即拷贝的结点
		if node == None:
			return None
		return self.dfs(node,map)
	def dfs(self, node, map):
		#如果已经访问过了就返回
		if node in map:
			return map[node]

		copynode = UndirectedGraphNode(node.label)
		map[node] = copynode
		for i in node.neighbors:
			copynode.neighbors.append(self.dfs(i,map))
		return copynode