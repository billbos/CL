#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# PCL1-Ü2-Aufgabe 5
# Vorlage von Raphael Balimann (raphael.balimann@uzh.ch) - HS 2015
#
# Authors:
# Bill Bosshard (12-933-255)
# Lukas Vollenweider (13-751-888)
#

# Eingabe des Names vom Nutzer, jedoch nur Nachname, danach Begrüssung durch Programm
lastname = raw_input('Bitte gebe deinen Nachnamen ein: ')
firstname = raw_input('Bitte gebe deinen Vornamen ein: ')
print "Hallo", firstname, lastname

# Vermessung der Eingabe
length = len(lastname)

print "Ihr Nachname hat", length, "Zeichen"

# Ausgabe je nach Länge des Namens, jedoch relativ ungenau
if (length >= 8):
	print "Auf Wiedersehen", lastname
elif ((length >= 5) & (length < 8)):
	print "Auf Wiedersehen", firstname, lastname
else:
	print "Auf Wiedersehen", firstname
