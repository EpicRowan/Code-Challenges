def vowels(str):
	count = 0
	vowels = "aeiou"
	for i in range(len(str)-1):
		if str[i] and str[i+1] and str[i+2] in vowels:
			count += 1
	return count


import re
def threevowels(string):
	arr = string.split('')
	count = 0
	for word in arr:
		if re.search(r'[aeious]{3,}', word) != None
		count += 1
	return count