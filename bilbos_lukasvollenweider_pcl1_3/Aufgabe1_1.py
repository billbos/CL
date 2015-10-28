#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 3, HS15
#Aufgabe 1.1
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888

text = ['Programmieren', 'macht', '%', 'Spass', 'und', 'ist', 
			'sehr', 'spannend','.', 'Jetzt', 'wollen', 'wir', 'den', 
			'Umgang', 'mit', 'Listen', 'verstehen']

#1.1.a)
text.append('!')

#1.1.b)
text.append('Dies')
text.append('ist')
text.append('mein')
text.append('Satz')

#1.1.c)
counter = 0
for item in text:
	if (item == 'ist'):
		counter = counter + 1
print "'ist' occurs", counter, "times"
	
#1.1.d) 
for position in range(0, len(text)):
	if (text[position] == '%'):
		del text[position]
		#we use break to be sure to only remove the first occurrence of '%'
		break

#1.1.e)
#from the python documentation:
# array.insert(i, x)
# Insert a new item with value x in the array before position i.
#therefore we need to use the third position --> 0,1,2
text.insert(2, 'so')

#1.1.f)
text[0] = 'Computerlinguistik'

#1.1.g)
position = 0
#we iterate through the list until we encounter "sehr" for the first time
while (text[position] != 'sehr'):
	position = position + 1
text[position] = 'unglaublich'

#uses ' ' as separator between the elements of text
print ' '.join(text)