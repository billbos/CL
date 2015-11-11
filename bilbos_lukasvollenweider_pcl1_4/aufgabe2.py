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

#check if input argument is a file or a string
#if it is a string, we store it in a list nonetheless because
#than we can use the same procedure for both input types
def commandline_argument():
	if re.search(r".txt$", userargument):
		return open(userargument, 'r')
	else:
		return [userargument]

#method which removes the \n if it finds one
#we have to do that to get the correct length back
def fixNewline(string):
	if re.search(r"\n$", string):
		return string[:-1]
	else:
		return string

if __name__ == "__main__":
	for line in commandline_argument():
		#remove \n at the end of the line (if it has one)
		line = fixNewline(line)
		#a flag which indicates if we found an ending
		did_match = False
		for ending in endings:
			#add '$' to the endings since we want it to be at the end of the line (-> word)
			if re.search(ending + r'$', line):
				#Successful match
				did_match = True
				up_to = len(line) - len(ending)
				#print until we reach the ending
				print line[0:up_to], "->", ending
		#if the word does not contain an ending from the list, we print the whole word
		if (not did_match):
			print line