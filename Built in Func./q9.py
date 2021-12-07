"""
map(function, iterable, ...) Apply function to every item of iterable and return a list.

Examples

  # convert each character to ASCII code using 'ord'
  >>>map(ord, 'abcde')
  [97, 98, 99, 100, 101]
  >>>map(float, ['1.3', '1', '2')                # convert to floating point numbers
  [1.3, 1.0, 2.0 ]
  >>>def add(x, y):
  ...     return x+y
  ...
  >>>map(add, [1, 2, 3], [4, 5, 6])              # function is 'add'
  [5, 7, 9]
  >>>map(lambda x,y:x+y, [1, 2, 3], [4, 5, 6])   # using lambda
  [5, 7, 9]
  >>>mapfn1(range(10, 12)]                       # convert to hex
  ['0xa', '0xb', '0xc']
  >>>mapfn2(range(10)]                           # modulo 2
  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
  >>>mapfn3(['pyschools'])                       # convert to uppercase
  ['P', 'Y', 'S', 'C', 'H', 'O', 'O', 'L', 'S']
"""
# Complete the code below so that the outputs are as shown in the examples above.


def mapfn1(alist):
    return map(lambda x: hex(x), alist)


def mapfn2(alist):
    return map(lambda x: x % 2, alist)


def mapfn3(word):
    return map(lambda x: x.upper(), word)


if __name__ == "__main__":
    print(list(mapfn2(range(10))))
    print(list(mapfn3(['pyschools'])))
