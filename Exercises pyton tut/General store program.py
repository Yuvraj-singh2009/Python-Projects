
store = {"item'sname":[],"quantity":[],"amount":[]}
b = list(store.values())
it= b[0]
qu = b[1]
am = b[2]

while True:
	try:
		check = int(input("Enter 1 for adding items \n Enter 2 for quitting \n"))

	except ValueError:
		print("Enter only number not string")
	try:
		if check == 1:
			items = str(input("Enter your item = "))
			quantity1 = int(input("Enter quantity = "))
			amount1 = int(input("Enter item's amount = "))
			it.append(items)
			qu.append(quantity1)
			am.append(amount1)	
	except:
		print("Here, you give wrong input")
	
		
	if len(qu) > 1:
		user = input("Enter yes or no")
		if user == "yes":
			print("ok")
			print("Ok then i will show you what is in your bucket list")
			for i in range(0,len(it)):

				print("items", i+1, ":",it[i] )
				print("quantity of your items is ", ":", qu[i],"Pieces")
				print("amount of your items is ", ":", am[i],"Rupees")
			print("Thanks for using it, Have a good day")
			# print("item", i ,":", list[i])
			
			break
		elif user == "no":
			print("ok then continue")
			continue
	


	
		

