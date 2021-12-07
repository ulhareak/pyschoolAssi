"""# Write a function that returns minimum and maximum values of a
list containing numbers in integer and string formats."""


def mixedList(mlist):
    """Returns min and max from the list."""
    for i in range(len(mlist)):
        mlist[i] = int(mlist[i])
    return (min(mlist), max(mlist))


if __name__ == "__main__":
    print(mixedList(["3", -3, 3, "-1"]))
