# A|B, where A and B are arbitrary REs, creates a regular expression that matches either A or B.

import re
re.findall('abc|123', '123def')  # matches 'abc' or '123'
# ['123']
re.findall('abc|123', '456abc')
# ['abc']
re.findall('abc|123', 'a1b2c3')
# []
#re.findall(regex, target)
#['org', 'edu', 'com']

regex = "com|edu|org"
target = "comeduorg"
print(re.findall(regex, target))
