#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 4, HS15
#Aufgabe 3
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888

import sys
#is needed for our sorting function
import operator

file1 = sys.argv[1]
file2 = sys.argv[2]
#has to be either "key" or "value"
sorting_mode = sys.argv[3]

#{word:#_of_occurrences}
words_from_file1 = {}
words_from_file2 = {}

#{word:#_of_occurrences}
words_from_both = {}


def read_words_from_file_into_hash(file, hash):
	for line in open(file, 'r'):
		#we split the line at the spaces to get the single words
		for word in line.split():
			#we add the # of occurrences to the hash for each word
			if (hash.has_key(word)):
				hash[word] = hash[word] + 1
			else:
				hash[word] = 1

def sort_hash(hash, sort_type):
	if (sort_type == "key"):
		sorting_key = 0
	else:
		sorting_key = 1
	#itemgetter gets the item at position sorting_key which then is used as sorting key
	#therefore if we use "key" as sort_type, the hash is sorted by alphabetical order
	#otherwise it is sorted by numeric order
	return sorted(hash.items(), key = operator.itemgetter(sorting_key))


def compareTwoHashes(hash1, hash2):
	for key1, value1 in hash1.items():
		#if we find the word from hash1 in hash2
		#we add both # of occurrences and save the result in a new hash
		if (hash2.has_key(key1)):				
			words_from_both[key1] = words_from_file1[key1] + words_from_file2[key1]

if __name__ == "__main__":
	read_words_from_file_into_hash(file1, words_from_file1)
	read_words_from_file_into_hash(file2, words_from_file2)

	compareTwoHashes(words_from_file1, words_from_file2)

	sorted_result = sort_hash(words_from_both, sorting_mode)
	#Annahme: Häufigkeiten --> Häufigkeit in file 1 und file 2 sollen getrennt dargestellt werden
	#Zum sortieren wird jedoch die kombinierte Häufigkeit verwendet
	print "Following words appear in both files:"
	for item in sorted_result:
		number_of_spaces = len(item[0])
		print item[0] + ": # of occurences in File1:", words_from_file1[item[0]], "\n" + ' ' * number_of_spaces," # of occurrences in File2:", words_from_file2[item[0]]
