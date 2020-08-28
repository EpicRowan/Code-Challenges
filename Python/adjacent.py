
def remove_adjacent(str):
	new = ''
	for i in range(len(str)-1):
		if str[i] != str[i+1]:
			new += str[i]
	return new 


