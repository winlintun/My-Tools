# find largest value on array


mylist = [5, 10, 21, 12, 8, 14, 1]

# linear search algothrim
def find_max_value_in_list(mylist:list):
	max_value = 0

	for data in mylist:
		if data > max_value:
			print("list data: ", data, "> ", max_value)
			max_value = data
		
	print(mylist)
	print("max_value: ", max_value)


def find_min_value_in_list(mylist:list):
	min_value = mylist[0]

	for data in mylist:  # not need sort
		if data >= min_value:
			min_value = min_value
		else:
			min_value = data
		print("list data: ", data, "> ", min_value)

	print(mylist)
	print("min_value: ", min_value)	


def reverse_in_list(mylist:list):
	for i in mylist:
		return mylist[::-1]


def sort_list(mylist:list):
	for i in range(len(mylist)):
		for j in range(i+1, len(mylist)):
			if mylist[i] > mylist[j]:
				print(mylist[i], mylist[j])
				mylist[i], mylist[j] = mylist[j], mylist[i]
