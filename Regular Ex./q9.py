# (...) matches whatever RE inside the parentheses.
# \number (starts from index 1) refers to the RE matched in preceding RE group.
# As '\' is used to escape special characters or to signal a special sequence (e.g. \d),
# it is a good practice to specify 'r' in front of RE to indicate raw strings.

import re
# match a odd number followed by a letter
re.findall('([13579])([a-z])', '1a2b3c')
#[('1', 'a'), ('3', 'c')]
# return a list of repeated numbers. Without 'r', need to backslash the '\'.
re.findall('([0-9])\\1', '1233455')
#['3', '5']
re.findall(r'([0-9])\1', '1233455')  # return a list of repeated numbers.
#['3', '5']
#re.findall(regex, 'a1bb222c3dd444')
#[('b', '2'), ('d', '4')]

# Complete the RE below to match the output of the above example.
regex = r"(\w)\1(\d)\2\2"
print(re.findall(regex, 'a1bb222c3dd444'))
