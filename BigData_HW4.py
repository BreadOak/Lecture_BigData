# BigData_HW4

word_list = []
Num_words = int(input("Enter Number of Words : "))

for i in range(1,Num_words+1):
	word = input("type word : ")
	word_list.append(word)

while(1):

	print("list : ",word_list)
	print("1:sort, 2:revese, 3:quit")

	Num = int(input("enter only number : "))

	if Num == 1:
		word_list.sort()

	elif Num == 2:
		word_list.reverse()

	elif Num == 3:
		break