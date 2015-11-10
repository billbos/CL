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
sorting = sys.argv[3]

#{word:#_of_occurrences}
words_from_file1 = {}
words_from_file2 = {}

#{word:#_of_occurrences}
words_from_both = {}


def read_words_from_file_into_hash(file, hash):
	for line in open(file, 'r'):
		for word in line.split():
			#we already count the number of occurrences of the words
			#because it saves us a lot of time afterwards
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
	#we first sort the two hashs by alphabetical order since comparing tuples is faster
	#than comparing hashes
	sorted_hash1 = sort_hash(hash1, "key")
	sorted_hash2 = sort_hash(hash2, "key")

	for item1 in sorted_hash1:
		for item2 in sorted_hash2:
			if (item2[0] == item1[0]):
				word_count = 0
				#if the items are equal, we check in which hash the word
				#appears less often. This is the value we need for word_count
				if (item2[1] > item1[1]):
					word_count = item1[1]
				else:
					word_count = item2[1]
				words_from_both[item2[0]] = word_count

if __name__ == "__main__":
	read_words_from_file_into_hash(file1, words_from_file1)
	read_words_from_file_into_hash(file2, words_from_file2)

	compareTwoHashes(words_from_file1, words_from_file2)

	sorted_result = sort_hash(words_from_both, sorting)

	print "Following words appear in both files:"
	for item in sorted_result:
		print item[0] + ":", item[1]
