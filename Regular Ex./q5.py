# [ ] is used to indicate a set of characters. Characters can be listed individually,
# or a range of characters can be indicated by '-' between two starting and end characters.
# If the first character is "^", it indicates the complement set.

import re
re.findall('[aeiou]', 'hello')   # search for vowels
#['e', 'o']
re.findall('[3-6]', '12345678')  # search for numbers 3-6
#['3', '4', '5', '6']
re.findall('[^3-6]', '12345678')  # search for complement set of numbers 3-6
#['1', '2', '7', '8']

regex_1 = '[a-z]'  # match a to z
regex_2 = '[A-Z]'  # match A to Z
regex_3 = '[a-zA-Z0-9]'  # match alphanumeric characters
