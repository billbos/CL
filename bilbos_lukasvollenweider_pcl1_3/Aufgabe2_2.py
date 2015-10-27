import string

longestWord = "gesundheitsweiderherstellungsmittelmischungsveraeltniskundiger"

for char in longestWord:
	letter_pos = string.lowercase.index(char)
	print char * (letter_pos + 1)