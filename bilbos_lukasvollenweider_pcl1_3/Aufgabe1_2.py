userInputs = []
foundWords = []
counterWords = 0

while (counterWords <= 150):
	usrinp = raw_input("Please enter a 4-letter ending you want to look for:")
	if (len(usrinp) != 4):
		continue
	for char in usrinp:
		if (char.isdigit()):
			continue
	if (usrinp not in userInputs):
		userInputs.append(usrinp)
	else:
		continue
	counterInput = 0
	for line in open('kafka_trial.txt', 'r'):
		words = line.split(' ')
		for word in words:
			if (word[len(word)-4:] == usrinp):
				foundWords.append(word)
				counterWords = counterWords + 1
				counterInput = counterInput + 1

	if (counterWords > 5):
		print "The ending '", usrinp, "'was found ", counterInput, " times."
		print "You have found more than 150 words"

		print "You entered following", len(userInputs), "endings:" 
		for input in userInputs:
			print input
		uniqueWords = set(foundWords)
		print "You found ", len(uniqueWords), "words" 
		sortedList = sorted(uniqueWords, key=len, reverse=True)
		print "The 5 longest words are: "
		for position in range(0,5):
			print sortedList[position], "length:", len(sortedList[position])
	else:
		counterWords - counterInput
	