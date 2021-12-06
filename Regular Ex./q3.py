# The '*' character matches 0 or more repetitions of the preceding RE.
# The '+' character matches 1 or more repetitions of the preceding RE.
# The '?' character matches 0 or 1 repetition of the preceding RE.

import re
re.findall('.*', 'abcd')  # match any number of characters
# ['abcd', '']  # additional '' because '*' matches zero character or empty string.
re.findall('.+', 'abcd')  # match 1 or more characters
# ['abcd']
re.findall('.?', 'abcd')  # match 0 or 1 character
#['a', 'b', 'c', 'd', '']

# What are the values of variables a, b and c in the following examples?

a = re.findall('..*', 'aeroplane')
b = re.findall('..+', 'aeroplane')
c = re.findall('..?', 'aeroplane')

if __name__ == "__main__":
    print(a)
    print(b)
    print(c)
