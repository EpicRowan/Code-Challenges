def vowels(str):
	count = 0
	vowels = "aeiou"
	for i in range(len(str)-1):
		if str[i] and str[i+1] and str[i+2] in vowels:
			count += 1
	return count
