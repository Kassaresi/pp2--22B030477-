#REGEX
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

# findall - Returns a list containing all matches
# search - Returns a Match object if there is a match anywhere in the string
# split - Returns a list where the string has been split at each match
# sub - Replaces one or many matches with a string

# [] - A set of characters	"[a-m]"	Try it »
# \	- Signals a special sequence (can also be used to escape special characters)	"\d"	Try it »
# .	- Any character (except newline character)	"he..o"	Try it »
# ^	- Starts with	"^hello"	Try it »
# $	- Ends with	"planet$"	Try it »
# *	- Zero or more occurrences	"he.*o"	Try it »
# +	- One or more occurrences	"he.+o"	Try it »
# ?	- Zero or one occurrences	"he.?o"	Try it »
# {} - Exactly the specified number of occurrences	"he.{2}o"	Try it »
# |	- Either or	"falls|stays"	Try it »
# () - Capture and group

# \A - Returns a match if the specified characters are at the beginning of the string	"\AThe"	Try it »
# \b - Returns a match where the specified characters are at the beginning or at the end of a word(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"r"ain\b"	Try it »
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"	Try it »
# Try it »
# \d - Returns a match where the string contains digits (numbers from 0-9)	"\d"	Try it »
# \D - Returns a match where the string DOES NOT contain digits	"\D"	Try it »
# \s - Returns a match where the string contains a white space character	"\s"	Try it »
# \S - Returns a match where the string DOES NOT contain a white space character	"\S"	Try it »
# \w - Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	Try it »
# \W - Returns a match where the string DOES NOT contain any word characters	"\W"	Try it »
# \Z - Returns a match if the specified characters are at the end of the string	"Spain\Z"