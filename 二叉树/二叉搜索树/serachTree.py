class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class SearchTree:
	def insert(self,data,node):
		if node == None:
			return TreeNode(data)
		elif data > node.val:
			node.right = self.insert(data,node.right)
			return node
		else:
			node.left = self.insert(data,node.left)
			return node
	def __init__(self,data):
		if data == []:
			self.root = None
			return
		self.root = TreeNode(data[0])
		for i in data[1:]:
			self.insert(i,self.root)
	#递归版二叉搜索树查找
	def find_recurs(self,x,cur_node):
		if x>cur_node.val:
			return self.find_recurs(x,cur_node.right)
		elif x<cur_node.val:
			return self.find_recurs(x,cur_node.left)
		else:
			return cur_node
	#循环版查找
	def find_loop(self,x,cur_node):
		while cur_node != None:
			if x>cur_node.val:
				cur_node = cur_node.right
			elif x<cur_node.val:
				cur_node = cur_node.left
			else:
				return cur_node
		#没找到
		return None
	def Find_max(self,node):
		while node.right != None:
			node = node.right
		return node
	def delete_node(self,x,cur_node):
		if cur_node == None:
			return False
		elif x < cur_node.val:
			cur_node.left = self.delete_node(x,cur_node.left)
			return cur_node
		elif x > cur_node.val:
			cur_node.right = self.delete_node(x,cur_node.right)
			return cur_node
		else:
			if (cur_node.left != None) & (cur_node.right != None):
				#让左子树中最大的变成替死鬼
				del_node = self.Find_max(cur_node.left)
				cur_node.val = del_node.val
				del_node.val = x
				cur_node.left = self.delete_node(x,cur_node.left)
				return cur_node
			else:
				del_node = cur_node
				#如果左儿子不为空, 让左儿子代替自己
				if cur_node.left != None:
					cur_node = cur_node.left
				else:
					#如果右儿子不为空或者都为空, 让右儿子代替自己
					cur_node = cur_node.right
				del del_node
				return cur_node
	def node_del(self,x):
		self.root = self.delete_node(x,self.root)
st = SearchTree([1,2,3,4,5])
node = st.find_loop(2,st.root)
st.node_del(2)
print(st.root.right.right.val)