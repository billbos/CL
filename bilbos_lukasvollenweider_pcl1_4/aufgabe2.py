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

#TOOD: Filterfunktion (?)

endings = ["ing", "s", "ed"]
filename = sys.argv[1]

for line in open(filename, "r"):
	#a flag which indicates if we found an ending
	did_match = False
	for ending in endings:
		#add '$' to the endings since we want it to be at the end of the line (-> word)
		if re.search(ending + r'$', line):
			#Successful match
			did_match = True
			print line[0:((len(line)-1)-len(ending))], "->", ending
	#if the word does not contain an ending from the list, we print the whole word
	if (not did_match):
		print line