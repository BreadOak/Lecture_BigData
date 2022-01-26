# BigData_HW6

# Write
file = open("/home/breadoak/BigData_Basic/introduce.txt",'a')
while(1):

	Item = input("Item(e:exit): ")

	if Item == "e":
		break

	else:
		Contents = input("Contents: ")
		file.write("* %s : %s\n" %(Item,Contents))
file.close()

# Read
file = open("/home/breadoak/BigData_Basic/introduce.txt",'r')
data = file.read()
print(data)
file.close()
