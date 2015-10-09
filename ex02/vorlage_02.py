#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# PCL1-Ü2-Aufgabe 5
# Vorlage von Raphael Balimann (raphael.balimann@uzh.ch) - HS 2015
#


# Eingabe des Names vom Nutzer, jedoch nur Nachname, danach Begrüssung durch Programm
lastname = raw_input('Bitte gebe deinen Nachnamen ein: ')
surname = raw_input('Bitte gebe deinen Vornamen ein: ')
print "Hallo", surname, lastname

# Vermessung der Eingabe
length = len(lastname)

print "Ihr Nachname hat", length, "Zeichen"

# Ausgabe je nach Länge des Namens, jedoch relativ ungenau
if (length >= 8):
	print "Auf Wiedersehen", lastname
elif ((length >= 5) & (length < 8)):
	print "Auf Wiedersehen", surname, lastname
else:
	print "Auf Wiedersehen", surname
