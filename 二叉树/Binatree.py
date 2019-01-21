class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class SearchTree:
	def __init__(self,data):
		self.root = TreeNode(data[0])
		i=1
		queue = [] #装结点
		queue.append(self.root)
		while (len(queue)!=0):
			#取出来
			tnode = queue.pop(0)
			#构造儿子结点
			if i>= len(data):
				continue
			tnode.left = TreeNode(data[i])
			i += 1
			if i>= len(data):
				continue
			tnode.right = TreeNode(data[i])
			i += 1
			#放入队列
			queue.append(tnode.left)
			queue.append(tnode.right)