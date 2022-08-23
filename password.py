password = 'a123456'
i = 3 #i代表剩餘機會
while i > 0:
	question = input('Please insert password:')
	if question == password:
		print('Succesfully login')
		break
	else:
		i = i - 1
		print('Wrong password! ',i ,'time left') 
		