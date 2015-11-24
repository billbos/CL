#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 5, HS15
#Aufgabe 3.2
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888

import nltk
from nltk.corpus import webtext
text6 = webtext.words('grail.txt')

def long_words(text):
	return sorted([word.lower() for word in set(text) if word >= 7 and word[-3:] == "ing"])

def tuples(text):
    return [(word, len(word)) for word in set(text)]

def trigrams(text):
   	return [(text[i-2], text[i-1], text[i]) for i in range(2, len(text))]

print "long_words: ",long_words(text6)[:10]
print "tuples: ", tuples(text6)[:10]
print "trigrams: ", trigrams(text6)[:10]