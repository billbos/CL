#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 3, HS15
#Aufgabe 1.2
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888

userInputs = []
foundWords = []
#keeps track of the total occurrences
# if > 150, we stop
counterWords = 0

while (counterWords <= 150):
	usrinp = raw_input("Please enter a 4-letter ending you want to look for:")
	#check if input is valid
	#if not, we just start the whole while loop again
	if (len(usrinp) != 4):
		continue
	for char in usrinp:
		if (char.isdigit()):
			continue
	#check if we already searched for the current usrinp
	#if yes, we jsut start the whole while loop again
	if (usrinp not in userInputs):
		userInputs.append(usrinp)
	else:
		continue

	#keeps track of the occurrences of usrinp
	counterInput = 0
	for line in open('kafka_trial.txt', 'r'):
		words = line.split(' ')
		for word in words:
			if (word[len(word)-4:] == usrinp):
				foundWords.append(word)
				counterInput = counterInput + 1
	#we only accept the words with 5 or more occurrences
	if (counterInput > 5):
		print "The ending '" + usrinp+ " 'was found ", counterInput, " times."
		counterWords = counterWords + counterInput

print "You have found more than 150 words"

print "You entered following", len(userInputs), "endings:" 
for input in userInputs:
	print input
uniqueWords = set(foundWords)
print "You found ", len(uniqueWords), "words" 
#we compare the words in uniqueWords with the len() functin (--> key=len) and reverse the
#result to get the longest ones first
sortedList = sorted(uniqueWords, key=len, reverse=True)
print "The 5 longest words are: "
for position in range(0,5):
	print sortedList[position], "length:", len(sortedList[position])
	