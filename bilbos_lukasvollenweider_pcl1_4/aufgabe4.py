#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 4, HS15
#Aufgabe 4
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888
import sys
import operator
import re 

database_path = sys.argv[2]
#either --file or --text
mode = sys.argv[3]
#either a file or a string
source = sys.argv[4]
database = {}

def parseDatabase(path):
	#Format (String, List) for an entry
	#Multiple possibilities for a word are in following format: word possibility1(occurrences)|possibility2(occurrences)
	for line in open(path, 'r'):
		word = ""
		extended_tags = []
		#separate word from tag
		words = line.split(' ')
		#we know that there are only 2 elements because of the way we formate the entries
		word = words[0]
		tags = words[1].split('|')
		for tag in tags:
			#we check how often a token was used
			#if there isn't a number, we assume it was used once
			#we save the word with the number in a tuple to be able
			#to access it later
			occurrences = re.search(r"\d+", str(tag))
			if occurrences is not None:
				extended_tags.append((re.search(r"[A-Z]+", str(tag)).group(0), int(occurrences.group(0))))
			else:
				extended_tags.append((re.search(r"[A-Z]+", str(tag)).group(0), 1))
		database[word] = extended_tags

#we ask the user every time we assume a tag
#even if it is already in the database because there could be
#a second possibility for the current word
#this method is only for words which are already in the database
def checkTag(word, tag):
	print "Is '" + word + "' a", database[word][tag][0] + "?"
	#we ask the user for confirmation in a while loop to trap him
	#until he gives a correct input
	while True:
		userinput = raw_input("Is this guess correct? ('Y' for yes, 'N' for no): ")
		if userinput == "Y":
			#if our guess was correct, we increase the counter by 1 and return the word with the new counter
			database[word][tag] = (database[word][tag][0],database[word][tag][1] + 1)
			return (word, tag)
		elif userinput == "N":
			#if our guess was not correct, we ask the user for the solution
			solution = raw_input("Please enter the correct STTS-Tag: ")
			#we check if the solution tag is already in our database
			#if yes, we increase the counter
			#if not, we create a new tag for the word
			for i in range(0, len(database[word])):
				if database[word][i][0] == solution.upper():
					database[word][i] = (database[word][i][0], database[word][i][1] + 1)
					return (word, solution.upper())
				database[word].append((solution.upper(),1))
				return (word, solution.upper())

def analyse_word(word):
	#Critera are partly from the solutions of assignment 2
	regex_pattern = []

	#we add the regex pattern to a list to be able to iterate through it
	#one can influence the result by appending the tags with a higher possibility
	#before the tags with a low possibility
	#we also append the tag as part of the tuple to be able to easily return the tag
	#if we get a match
	regex_pattern.append((r"^\d+$", "CARD"))
	regex_pattern.append((r"^(der|die|das|eine?n?)$", "ART"))
	regex_pattern.append((r"^(und|oder|aber)$", "KON"))
	regex_pattern.append((r"^nicht$", "PTKNEG"))
	regex_pattern.append((r"^(als|wie)$", "KOKOM"))
	regex_pattern.append((r"^(ich|du|er|sie|es|wir|ihr)$", "PPER"))
	regex_pattern.append((r"^(meine?s?|deine?s?|seine?s?|ihre?s?|unsere?s?|euer)$", "PPOS"))
	regex_pattern.append((r"[a-z]+sten$", "ADJA"))
	regex_pattern.append((r"^[a-z]\w*en$", "VVINF"))
	regex_pattern.append((r"^[a-z]\w*(t(e)?)?$", "VVFIN"))
	regex_pattern.append((r"[A-Z]\w*(heit|keit|er)?$", "NN"))

	for pattern in regex_pattern:
		match = re.search(pattern[0], word)
		if match is not None:
			return pattern[1]
	return None

def tag_word(word):
	#check if the word is already in the database
	if (database.has_key(word)):
		#check if there are more than one possibility
		if len(database[word]) > 1:
			#check which tag has the highest counter and choose it as guess
			tag_with_highest_possibility = 0
			for i in range(0, len(database[word])):
				if database[word][i][1] > database[word][tag_with_highest_possibility][1]:
					tag_with_highest_possibility = i;
			checkTag(word, tag_with_highest_possibility)
		elif (len(database[word]) == 1):
			checkTag(word, 0)
	else:
		result_tag = analyse_word(word)
		#if we get a match, we ask if our guess is correct
		#and add either the guess if it was correct
		#or the solution if it was not correct to the database
		if result_tag is not None:
			print "Is '" + word + "' a", result_tag + "?"
			while True:
				userinput = raw_input("Is this guess correct? ('Y' for yes, 'N' for no): ")
				if userinput == "Y":
					database[word] = (result_tag,1)
					return (word, result_tag)
				elif userinput == "N":
					solution = raw_input("Please enter the correct STTS-Tag: ")
					#we use upper() to cast lowercase letters to uppercase
					database[word] = (solution.upper(), 1)
					return (word, solution.upper())
		#if we did not get a match, we ask for the solution
		elif result_tag is None:
			solution = raw_input("Please enter the correct STTS-Tag: ")
			database[word] = (solution.upper(), 1)
			return (word, solution.upper())

def print_sentence(sentence):
	#we print each sentence in the following format:
	#word\tag word\tag word\tag
	for word in sentence:
		sys.stdout.write(word[0] + '\\' + word[1] + " ")
	sys.stdout.write("\n")

def read_sentence(source, mode):
	#Annahme: Keine Abkürzungen
	#contains all sentences
	output = []
	text = ""
	if mode == "--file":
		text = open(source, 'r').read()
	else:
		text = source
	#we assume that our text does not have any abbreviations
	for sentence in text.split('.'):
		print sentence
		#contains current sentence
		annotated_sentence = []
		for word in sentence.split(' '):
			#there is a bug after a newline char where 
			#the first word in the second sentence is empty
			#therefore we check with regex if our word is actually a word
			if re.search(r"^\w+$", word):
				annotated_sentence.append(tag_word(word))
		output.append(annotated_sentence)

	for sentence in output:
		print_sentence(sentence)
			

if __name__ == "__main__":
	parseDatabase(database_path)
	read_sentence(source, mode)
