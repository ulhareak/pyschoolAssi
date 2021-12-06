# Return a list of all non-overlapping matches of pattern in string.

import re
a = re.findall('e', 'telephone')
b = re.findall( 'epho','telephone')

print(a)
print(b)