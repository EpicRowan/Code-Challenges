
def recursive_factorial(num):
	if num == 1:
		return 1
	return num * recursive_factorial(num-1)