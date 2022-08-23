password = 'a123456'
i = 3 #i代表剩餘機會
while i > 0:
	i = i - 1
	question = input('Please insert password:')
	if question == password:
		print('Succesfully login')
		break
	else:
		print('Wrong password!') 
		if i > 0:
			print( i ,'time left')
		