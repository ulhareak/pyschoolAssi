# The '.' character matches any character except a newline. To match a newline, specify 'DOTALL' in the flag.
# The '^' character matches the start of the string.
# The '$' character matches the end of the string.

import re
re.findall('.', 'abcd')   # match any character
#['a', 'b', 'c', 'd']
re.findall('^a', 'abcd')  # match only if 'a' is at start of line
# ['a']
re.findall('^d$', 'abcd')  # match if 'd' is the only character in a line.
[]

# What are the values of 'a' and 'b' in the following examples?

a = re.findall('..$', 'aeroplane')
b = re.findall('^.', 'computer')

if __name__ == "__main__":
    print(a)
    print(b)
