userinput = raw_input("Bitte gebe ein (langes) Wort ein:")

for x in range(0, len(userinput)):
	print x * ' ', userinput[:x]
for x in range(0, len(userinput)):
	print (len(userinput) - x) * ' ', userinput[:len(userinput) - x]
