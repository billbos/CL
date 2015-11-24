#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 5, HS15
#Aufgabe 3.1c
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888

import nltk

from nltk.book import *
from nltk.corpus import webtext

text6 = webtext.words("grail.txt")

def findVerbs(text):
	verbs = []
	for word in set(text):
		if len(word) >= 4 and word[-3:] == "ing":
			verbs.append(word.lower())
	return sorted(verbs)

if __name__ == "__main__":
	print findVerbs(text6)