# Fill in the RE below so that the resulting string will remove double vowel with single
# vowel.
import re
re.sub('\W', '', 'ab^c&d~1!2;3{')   # remove non-alphanumeric characters
# 'abcd123'
re.sub(r'([aeiou])', r'<b>\1</b>', 'zero')  # enclose vowels with <b>, </b>.
# 'z<b>e</b>r<b>o</b>'
# # remove repeating vowels.
# 'stop'

regex = r"([aeiou]) "
repl = r"[aeiou][aeiou]"
print(re.sub(regex, repl, 'stoop'))
