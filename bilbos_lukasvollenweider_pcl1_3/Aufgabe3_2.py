#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 3, HS15
#Aufgabe 3.2
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888

import sys

filename = sys.argv[1]
occurrences = {}

for line in open(filename, 'r'):
	#a)
	for word in line.split(' '):
		if (len(word) > 6):
			#b)
			if word in occurrences.keys():
				occurrences[word] = occurrences[word] + 1
			else:
				occurrences[word] = 1

#c
sortedList = sorted(occurrences.keys())

for key in sortedList:
	print key + "\t", occurrences[key]