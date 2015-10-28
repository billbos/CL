#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 3, HS15
#Aufgabe 3.1
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888

SAC = {'Schoenenberger':'Rigi', 'Zueberbuehler':'Pizol', 'Stepankova':'Pizol', 'Schmid':'Flumserberge',
       'Rutz':'Pilatus', 'Zimmerli':'Jungfrau', 'Bizirianis':'Pfannenstiel', 'Maurer':'Dom',
       'Ferrari':'Eiger', 'Wiedmer':'Pfannenstock', 'Helbling':'Platthorn' , 'Blickenstorfer':'Weisshorn'}

#Dein Code
SAC['A'] = 'test'

SAC['Schoenenberger'] = 'Rigi'
# es passiert nichts, da der wert mit dem schlüssel schon vorhanden ist

SAC['Schoenenberger'] = 'Eiger'
# der wert für den key schoenenberger wird mit eiger überschrieben
print SAC

for keys,values in SAC.items():
    print keys + "\t" + values

list_key = sorted(SAC.keys())

for key in list_key:
    if (len(SAC[key]) > 5):
        print key
        

