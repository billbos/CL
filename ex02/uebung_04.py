# Authors:
# Bill Bosshard (12-933-255)
# Lukas Vollenweider (13-751-888)

usrinpt = raw_input("Bitte taetigen Sie eine Eingabe (min. 5 Zeichen): ")

counter = 2
substring = ""
while (counter < 5):
	substring = substring + usrinpt[counter]
	counter = counter + 1
print substring

#########################################################################################
#										AUFGABEN										#
#########################################################################################
#																					  	#
#	a) Wenn die Eingabe weniger als 5 Zeichen besitzt, gibt es eine Fehlermeldung	  	#
#																					  	#
#	b) Nachdem der User eine Eingabe getaetigt hat, wird diese mit einem if ueberprueft #
#	   if (len(usrinpt) < 5):														  	#
#			usrinpt = raw:input("Eingabe zu kurz: Neue Eingabe mit MIN. 5 Zeichen: ") 	#
#	   else:																			#
#			fuehrt die Programmlogik ab counter = 2 aus									#															
#	   																					#
#########################################################################################
