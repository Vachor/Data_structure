def Fab(n):
	i = 0
	pre = 0
	cur = 1
	for i in range(n):
		temp = pre + cur
		pre = cur
		cur = temp
	return pre
for i in range(30):
	print(Fab(i),end=' ')