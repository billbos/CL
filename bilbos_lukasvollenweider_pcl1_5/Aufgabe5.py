#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 5, HS15
#Aufgabe 5
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888

import sys
import nltk, operator
from nltk.corpus import webtext


#Dein Code
word_length = int(sys.argv[1])
letter = sys.argv[2]

words_with_wordlength = {}
words_with_letter = {}

def printresult(dict):
	dict_sorted = sorted(dict.items(), key = operator.itemgetter(1)) #sortiert dict nach Wert
	#Dein Code


def main():
	text = webtext.words('grail.txt')
	#Dein Code¨

	for words in text:
		words = words.lower()
		if (len(words) == word_length):
			if (words_with_wordlength.has_key(words)):
				value = words_with_wordlength[words]
				words_with_wordlength[words] = value + 1
			else:
				words_with_wordlength[words] = 1
		if (words[0] == letter):
			if (words_with_letter.has_key(words)):
				value = words_with_letter[words]
				words_with_letter[words] = value + 1
			else:
				words_with_letter[words] = 1

	sorted_words_wordlength = sorted(words_with_wordlength.items(), key=operator.itemgetter(1), reverse=True)

	print "Häufigstes Wort mit", word_length, "Buchstaben:"
	print sorted_words_wordlength[0][0], ":", sorted_words_wordlength[0][1]

	sorted_words_letter = sorted(words_with_letter.items(), key=operator.itemgetter(1), reverse=True)

	print "Häufigstes Wort mit Anfangsbuchstabe", letter, ":"
	print sorted_words_letter[0][0], ":", sorted_words_letter[0][1]

	for words in sorted_words_wordlength:
		if (words[0][0] == letter):
			print "Häufigstes Wort mit", word_length, "Buchstaben und Angangsbuchstabe", letter + ":"
			print words[0], ":", words[1]
			break


if __name__ == "__main__":
	main()