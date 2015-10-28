#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 3, HS15
#Aufgabe 2.2
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888

import string

longestWord = "gesundheitsweiderherstellungsmittelmischungsveraeltniskundiger"

for char in longestWord:
	letter_pos = string.lowercase.index(char)
	#we have to add + 1 to letter_pos, since a is at position 0
	print char * (letter_pos + 1)