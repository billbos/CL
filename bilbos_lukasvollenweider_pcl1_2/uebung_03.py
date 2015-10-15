# -*- coding: utf-8 -*-
# Authors:
# Bill Bosshard (12-933-255)
# Lukas Vollenweider (13-751-888)

#Eingabe wird zu float konventiert, damit x und y nachher auch floatergebnisse sind
a = float(raw_input("Bitte geben Sie den a-Wert ein: "))
b = float(raw_input("Bitte geben Sie den b-Wert ein: "))
c = float(raw_input("Bitte geben Sie den c-Wert ein: "))

x = (a + b + 3) / c
y = (b - pow(a,b)) / x

print x
print y

#########################################################################################
#										AUFGABEN										#
#########################################################################################
#																					  	#
#	a) int --> ganze Zahlen ohne Nachkommastellen. Beispiel: 1. Ein Int kann also 		#
#			   keine Kommastellen darstellen					  						#
#	 float --> Gleitkommazahlen mit Nachkommastellen. Beispiel: 1.0						#		
#																	  					#
#	b) Bei einem integer werden alle Nachkommazahlen abgeschnitten. 				    #
#	   Beispiel: 3/2 = 1 und nicht 1.5 da .5 abgeschnitten wird. 					  	#
#	   Das fuehrt zu ungenauen und auch falschen Ergebnissen. 							#
#	   Deshalb sollte man Gleitkommazahlen für Bruchrechnungen verwenden, wenn man 		#
#	   genaue Loesungen braucht. 														#																			#
#	   																					#
#########################################################################################