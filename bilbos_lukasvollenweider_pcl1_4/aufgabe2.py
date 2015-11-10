#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 4, HS15
#Aufgabe 2
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888
import sys
import re

endings = ["ing", "s", "ed"]
userargument = sys.argv[1]

def commandline_argument():
	if re.search(r".txt$", userargument):
		return open(userargument, 'r')
	else:
		return [userargument]

def fixNewline(string):
	if re.search(r"\n$", string):
		return string[:-1]
	else:
		return string

if __name__ == "__main__":
	for line in commandline_argument():
	#a flag which indicates if we found an ending
		#remove \n at the end of the line (if it has one)
		line = fixNewline(line)
		did_match = False
		for ending in endings:
			#add '$' to the endings since we want it to be at the end of the line (-> word)
			if re.search(ending + r'$', line):
				#Successful match
				did_match = True
				up_to = len(line) - len(ending)
				print line[0:up_to], "->", ending
		#if the word does not contain an ending from the list, we print the whole word
		if (not did_match):
			print line