#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 3, HS15
#Aufgabe 1
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
		
#1.1.d) Annahme: & soll eigentlich % sein
for position in range(0, len(text) - 1):
	if (text[position] == '%'):
		del text[position]

#1.1.e)
text.insert(2, 'so')

#1.1.f)
text[0] = 'Computerlinguistik'

#1.1.g)
position = 0
while (text[position] != 'sehr'):
	position = position + 1
text[position] = 'unglaublich'

print ' '.join(text)