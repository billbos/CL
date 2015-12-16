#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 6, HS15
#Aufgabe 2
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888

import regex
import codecs

#from http://stackoverflow.com/a/14919377
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def split_string(string):
	"""
	Split a string into first and last name

	Args:
		string: A string which contains the last name (written in capital letters) followed by the first name

	Returns:
		Tuple: (last name, first name)
	"""
	first_name = ""
	last_name = ""

	last_name_pat = regex.search(ur"([^\p{Ll}]+)", str(string))
	if last_name_pat is not None:
		last_name = last_name_pat.group()[:-2].decode('utf-8').lower()

	first_name_pat = regex.search(ur"\p{Lu}{1}\p{Ll}{1}.*$", str(string))
	if first_name_pat is not None:
		first_name = first_name_pat.group()[:-1].decode('utf-8').lower()

	return (last_name, first_name, string[:-1])

def main():
	f = open("result.tsv", 'w')
	with codecs.open("NAME.tsv") as pos_tbl:
		for line in pos_tbl:
			result = split_string(line)
			f.write(result[1] + '\t' + result[0] + '\t' + result[2] + '\n')
	f.close()

if __name__ == "__main__":
    main()
