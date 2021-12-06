# search(pattern, string[, flags])
# Scans through string looking for a location where the RE pattern produces a match, and returns a corresponding
# MatchObject instance.


import re
regex1 = r"([\d]{2})[^0-9]([\d]{3})"
regex2 = r"(\w)\d{3}(\w)"

print(re.search(regex1, 'a1b22c333d4444').groups())
#('22', '333')
print(re.search(regex2, 'a1b22c333d4444').groups())
#('c', 'd')
