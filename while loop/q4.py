"""Create a function countPages(x) that takes the number of pages of a
 book as an argument and counts the number of times the digit '1' appears in the page number."""


def countPages(num):
    total = 0
    i = 1
    while i <= num:
        total += str(i).count('1')
        i += 1

    return total


if __name__ == "__main__":
    print(countPages(200))
    print(countPages(100))
    print(countPages(11))
