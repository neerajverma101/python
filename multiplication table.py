for col in range(1,11):
	print('{:>3}=|'.format(col),end="")
	for row in range(1,11):
		print('{:>4}'.format(col*row),end="") 

	if(col==1):	
		print('\n{:#^45}'.format("multiplication 10X10"),end="")
	print("");