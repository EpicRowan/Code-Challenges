
def reverse_string(str):
	return "".join([letter for letter in str if letter.isalpha()][::-1])

print(reverse_string("pie"))