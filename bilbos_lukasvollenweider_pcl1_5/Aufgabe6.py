#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 5, HS15
#Aufgabe 6
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888
import nltk
from nltk.corpus import brown

def get_categorie_min_max(freqDist, word, categories):
	""" Gets the categories in which the word occurres the most and the least

	Args:
		freqDist: frequency distributions of a word in a category
		word: the word we want the frequency of
		categories: the list of categories
	Returns:
		List of two Tuples, one containing the categories with the min occurrences, 
		the other the categories with the max occurrence
	"""

	min = 0
	max = 0
	min_cat = []
	max_cat = []
	init = True

	for cat in categories:
		if init:
			min = freqDist[cat][word]
			min_cat.append(cat)
			max = freqDist[cat][word]
			max_cat.append(cat)
			init = False
		else:
			temp = freqDist[cat][word]
			if temp == min:
				min_cat.append(cat)
			if temp == max:
				max_cat.append(cat)
			if temp > max:
				max = temp
				del max_cat[:]
				max_cat.append(cat)
			if temp < min:
				min = temp
				del min_cat[:]
				min_cat.append(cat)
	result = [(min, min_cat), (max, max_cat)]
	return result

def print_array(categories):
	""" helper function to print all categories from a list on a single line

	Args:
		categories: list of categories
	"""
	count = len(categories)

	if count == 1:
		print categories[0]
	else:
		for i in range(0, count):
			print categories[i],
			if i != count - 1:
				print ",",


def print_min_max_for_all(freqDist, words, categories):
	""" prints the categories in which the words occurre the most and the least

	Args:
		freqDist: frequency distributions of a word in a category
		word: the word we want the frequency of
		categories: the list of categories
	"""
	for word in words:
		result = get_categorie_min_max(freqDist, word, categories)
		print word
		print "Kategorie mit grösstem Anteil ist:"
		print_array(result[1][1])
		print "Kategorie mit kleinstem Anteil ist:"
		print_array(result[0][1])
		#print newline
		print

def main():
	#Annahme: Wort "heart" statt "fun"
	words = [u'money', u'duty', u'love', u'heart']
	categories = [u'science_fiction', u'romance', u'government', u'humor', u'religion']
	#Dein Code
	cfd = nltk.ConditionalFreqDist((genre, word)
			for genre in brown.categories()
			for word in brown.words(categories=genre))

	cfd.tabulate(conditions=categories, samples=words)

	print_min_max_for_all(cfd, words, categories)

if __name__ == "__main__":
	main()