# Authors:
# Bill Bosshard (12-933-255)
# Lukas Vollenweider (13-751-888)

import webbrowser

userinput = raw_input("Bitte gebe ein deutsches Wort ein, Abbruch mit 'q': ")

while (userinput != "q"):
	length = len(userinput)
	if (length - 4 > 0):
		if (userinput[length - 4:] == "heit"):
			print userinput, "ist ein Nomen."
		elif (userinput[length - 4:] == "sten"):
			print userinput, "ist ein Adjektiv im Superlativ"
		elif (userinput[length - 2] == "te"):
			print userinput, "ist ein Verb"
		else:
			url = "http://www.duden.de/rechtschreibung/" + userinput
			print webbrowser.open(url)
	else:
		if ((userinput[length - 2] > 0) & (userinput[length -2:] == "te")):
			print userinput, "ist ein Verb"
		else:
			url = "http://www.duden.de/rechtschreibung/" + userinput
			print webbrowser.open(url)
	userinput = raw_input("Bitte gebe ein deutsches Wort ein, Abbruch mit 'q': ")


