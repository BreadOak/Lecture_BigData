# BigData_HW5

NumBook = {}

while(1):
	print("=====================================")
	print("1: add, 2: search, 3: delete, 4: quit")
	print("=====================================")

	Num = int(input("enter only number : "))

	if Num == 1:
		name   = input("type name : ")
		number = input("type number : ")
		NumBook[name] = number

	elif Num == 2:
		name = input("find name : ")
		print("Name : ", name)
		print("Number : ", NumBook[name])

	elif Num == 3:
		name = input("delete name : ")
		del NumBook[name]

	elif Num == 4:
		break

	print("\n")
	print("NumberBook : ", NumBook)
	print("\n")
