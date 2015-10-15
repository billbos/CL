# -*- coding: utf-8 -*-

#PCL1-Ü2-Aufgabe 5
#ursprüngl. Katrin Affolter, modifiziert durch Adrian van der Lek, weiter modifiziert durch Raphael Balimann

#Autoren
#Bill Bosshard (12-933-255)
#Lukas Vollenweider (13-751-888)
#
#
#Gib hier an, was das Programm genau macht:
#
#Eingabe: Halbe Höhe des Diamanten, Zeichen mit dem der Diamant gezeichnet wird
#Ausgabe: Diamant aus Zeichen, das eingegeben wurde und der Höhe 2xEingabe. Wenn gross genug: SHINE in Loch
#

usrinput = raw_input('Please enter desired height of the diamond: ')
char = raw_input('Which character should be used? ')

#Hälfte der Höhe des Diamanten
var1 = int(usrinput)
#Anzahl Zeilen. -1, da bei 0 begonnen wird --> Zeilen 0 - 29
var2 = var1 * 2 - 1

#Aktuelle Zeile
varA = 0 

#Anzahl chars pro Zeile
varB = 1

#Anzahl Leerzeichen in der Mitte des Diamanten
varC = 0

#Abtrennung
print "\n----------------------------\n"

while ( varA < var1 ): 
	if (var1 - varA) < var1/2:
		varC +=2
		#SHINE wird nur ausgegeben, wenn die Leerzeichenanzahl in der Mitte mindestens 8 beträgt
		if var1 - varA == 1 and varC >= 8:
			#Anzahl Leerzeichen bis zu SHINE
			varD = (varC - 5)/2
			#(var2 - varB)/2): Einrücken, sodass chars zentriert werden 
			#char * (varB/2 - varC/2): Hälfte der chars - Hälfte der Abstande bis zur Mitte
			#nach der Mitte wird der Vorgang umgekehrt wiederholt 
			print " " * ((var2 - varB)/2) + char * (varB/2 - varC/2) + varD * " " + "SHINE" + varD * " " + char * (varB/2 - varC/2 + 2)
		else:
			print " " * ((var2 - varB)/2) + char * (varB/2 - varC/2) + varC * " " + char * (varB/2 - varC/2 + 1)
	else:
		#Einrücken, sodass chars zentriert sind
		print " " * ((var2 - varB)/2) + char * varB
	#nächste Zeile
	varA += 1
	#2 Zeichen mehr pro Zeile
	varB += 2

varA -= 1
varB -= 2
	
while ( varA >= 0 ): 
	#Nachdem SHINE ausgegeben wurde (oder auch nicht) nimmt die Anzahl Zeichen pro Zeile wieder ab
	if (var1 - varA) < var1/2:
		varC -=2
		print " " * ((var2 - varB)/2) + char * (varB/2 - varC/2) + varC * " " + char * (varB/2 - varC/2 + 1)
	else:
		print " " * ((var2 - varB)/2) + char * varB
	varA -= 1
	varB -= 2

#Abtrennung
print "\n----------------------------\n"
