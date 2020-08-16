
answer = "cute cats chase fuzzy rats"

def word_counts(answer):

	blank = {}
	words = answer.split


	for word in words:
		if len(word) not in blank:
			blank[len(word)] = word
		else:
            blank[len(word)] += " " + word

	return blank
