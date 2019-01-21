class Node:
	def __init__(self):
		self.n = None
		self.tag = None
def Fibnacci (N):
	S = []
	w = Node()
	sum = 0
	while(True):
		while ( N > 1 ):
			w.n = N
			w.tag = 1
			S.append (w)
			N -= 1
		#向左递归到底, 边走边进栈
		sum = sum + N
		while (len(S) != 0):
			w = S.pop()
			if (w.tag == 1):   #改为向右递归
				w.tag = 2
				S.append (w)
				N = w.n - 2
				break
		if len(S) <= 0:
			break
	return sum
print(Fibnacci(3))