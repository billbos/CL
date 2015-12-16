#!/usr/bin/env python
# -*- coding: utf-8 -*-
#PCL I, Übung 6, HS15
#Aufgabe 1.2
#Autor: Bill Bosshard
#Matrikel-Nr.: 12-933-255
#Autor: Lukas Vollenweider
#Matrikel-Nr.: 13-751-888

import unicodedata

class Normalstring(object):

	def __init__(self, string):
		"""
		Normalstring initializer

		Saves the string to a local variable 'unnormal'. 
		Also saves a normalized version of the input string in a local variable 'normal'

		Args:
			string: unicode string

		Returns:
			a Normalstring instance
		"""

		self.unnormal = string
		self.normal = self._normalize(string)

	def __eq__(self, other):
		"""
		Two Normalstrings are equal if there normalized version are equal

		Args:
			other: Normalstring to compare against

		Returns:
			true: if the strings are equal
			false: if not
		"""

		return self.normal == other.normal

	def __getitem__(self, i):
		"""
		Returns the normalized character from a Normalstring at position i 

		Args:
			String: normalized version of a string
			i: Position of the character

		Returns:
			Character at postion i
		"""

		return self.normal[i]

	def __contains__(self, other):
		"""
		Checks if self contains the other string

		Returns:
			True is self contains other
			False otherwise
		"""
		if (self.index(other) != -1):
			return True
		else:
			return False

	def __str__(self):
		"""
		String representation of Normalstring

		Returns:
			the normalized version of a string
		"""
		return self.normal

	def _normalize(self, string):
		"""
		Normalizes a unicode string

		Args:
			string: unicode string

		Returns:
			a normalized string
		"""
		nfkd_form = unicodedata.normalize('NFKD', string)
		return u"".join(c for c in nfkd_form if not unicodedata.combining(c))

	def index(self, string):
		"""
		Return the position of the first occurrence of a substring

		Args:
			string: Substring from which we want to know the position

		Returns:
			Positon if the string was found
			-1 otherwise
		"""

		normalized_substring = self._normalize(string)
		substring_length = len(normalized_substring)

		for i in range(0, len(self.normal)):
			if (self.normal[i:i + substring_length] == normalized_substring):
				return i
		return -1

