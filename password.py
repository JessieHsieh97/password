password = 'a123456'
i = 3
while True:
	question = input('Please insert password:')
	if question == password:
		print('Succesfully login')
		break
	else:
		i = i - 1
		print('Wrong password! ',i ,'time left') #i代表剩餘機會
		if i == 0:
			break



		


	
	
	

	    


