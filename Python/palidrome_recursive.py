
def is_palindrome(str):
	palindrome = True
	start = 0
	end = len(word) - 1

	while start < end:
		if word[start] != word[end]:
			palindrome = False
			break
		start += 1
		end -= 1
	return palindrome

