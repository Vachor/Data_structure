def recurs(a,n,chose):
	length = len(a)
	if n==length-1:
		if chose == False:
			return 0
		if chose == True:
			return 1

	if chose == False:
		return recurs(a,n+1,True)
	else:
		if a[n] <= a[n+1]:
			return recurs(a,n+1,True)+1
		else:
			return recurs(a,n+1,True)

print(recurs([1,7,3,5,9,4,8],0,True))