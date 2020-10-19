def get_all_substrings(string):
	length = len(string)
	alist = []
	for i in range(length):
		for j in range(i,length):
			alist.append(string[i:j + 1]) 
	return alist

def get_all_substrings_one_line(str):
	return [str[i:j+1] for i in range(len(str)) for j in range(i, len(str))]

def get_all_sublists(list):
	return [list[i:j+1] for i in range(len(list)) for j in range(i, len(list))]

print(get_all_substrings('abcde'))
print(get_all_substrings_one_line('abcde'))
print(get_all_sublists([1,2,3,4,5]))
