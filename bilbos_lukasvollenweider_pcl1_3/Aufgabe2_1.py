#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 3, HS15
#Aufgabe 2
#Autor: dein_name
#Matrikel-Nr.: deine_matrikel

import random
#kreiert eine Liste mit 300 randomisierten Zahlen zwischen 1 und 600
numbers = []
for i in range(301):
	numbers.append(random.randint(1,600))

#Dein Code
even = []
odd = []
for i in numbers:
	if (i % 2 == 0):
		even.append(i)
	else:
		odd.append(i)

print "# even numbers: "
print len(even)

print "# odd numbers: "
print len(odd)

evenSorted = sorted(even, reverse = True)
oddSorted = sorted(odd, reverse = True)

sumEven = 0
print "largest even numbers:"
for i in range(0,5):
	sumEven = sumEven + evenSorted[i]
	print evenSorted[i]

sumOdd = 0
print "largest odd numbers:"
for i in range(0,5):
	sumOdd = sumOdd + oddSorted[i]
	print oddSorted[i]

if (sumEven > sumOdd):
	print "the sum of the even numbers is larger:", sumEven
else:
	print "the sum of the odd numbers is larger:", sumOdd