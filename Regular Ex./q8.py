# \w matches any alphanumeric character and the underscore.
# \W matches the complement of \w.

import re
re.findall('\w', '%*2&3c_')
#['2', '3', 'c', '_']
re.findall('\W', '^12#3$_')
# ['^', '#', '$']
