"""
The split() function has the following syntax:

split(pattern, string, maxsplit=0, flags=0)

In this syntax:

pattern is a regular expression whose matches will be used as separators for splitting.
string is an input string to split.

maxsplit determines at most the splits occur. Generally, if the maxsplit is one, the
resulting list will have two elements. If the maxsplit is two, the resulting list will
have three elements, and so on.

flags parameter is optional and defaults to zero. The flags parameter accepts one or
more regex flags. The flags parameter changes how the regex engine matches the pattern.

The split() function returns a list of substrings split by the matches of the pattern
in the string.

If the pattern contains one or more capturing groups, the split() function will return
the text of all groups as elements of the resulting list.

If the pattern contains a capturing group that matches the start of a string, the split()
function will return a resulting list with the first element being as an empty string.
This logic is the same for the end of the string.
"""

# Python regex split() function examples

# 1) Using the split() function to split words in a sentence

import re # import regex

text = 'A! B. C D + E' # string of characters
pattern = r'\W+' 

list = re.split(pattern, text)
print(list)


# the \W+ is the inverse of the word character set that
# matches one or more characters that are not the word characters.