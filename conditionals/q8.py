"""
For a quadratic equation in the form of ax2 + bx + c, the discriminant, D is b2-4ac.
Write a function that return the following output depending on the discriminant.
D > 0: 2 real roots.
D = 0: 1 real root.
D < 0: 2 complex roots.
Examples

    >>> quadratic(1, 2, 3)
    'This equation has 2 complex roots.'
    >>> quadratic(1, 3, 2)
    'This equation has 2 real roots.'
    >>> quadratic(1, 4, 4)
    'This equation has 1 real root.'
"""


def quadratic(a, b, c):
    """ return roots and types acco. to discriminant. """
    d = (b*b) - 4*a*c
    r = ""
    if d > 0:
        r = 'This equation has 2 real roots.'
    elif d == 0:
        r = 'This equation has 1 real root.'
    else:
        r = 'This equation has 2 complex roots.'

    return r


def main():
	"""Works as a main function of program"""
    print(quadratic(1, 2, 3))
    print(quadratic(1, 3, 2))
    print(quadratic(1, 4, 4))


if __name__ == "__main__":
    main()
