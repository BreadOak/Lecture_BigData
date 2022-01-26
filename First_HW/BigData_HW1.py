# BigData_HW1

Total_Sum = 0

print("Enter '0' when all jobs are finished")

while(1):

	Number = int(input("Number : "))

	if Number%3 != 0:

		for i in range(1,Number+1): 
			Total_Sum = Total_Sum + i

		print("Total Sum : %d" % Total_Sum) 
		Total_Sum = 0

	elif Number == 0:
		print("Finish")
		break
