"""
Create a function genSet() that takes in a list of numbers and returns a sorted set.

Examples

    >>> genSet([5,4,8,4,9,8])
    [4, 5, 8, 9 ]
    >>> genSet([3,-2,-1,-1,3,-2,0])
    [-2, -1, 0, 3 ]
"""


def genSet(nums):
    """it generates the Soerted set from given list"""
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    return nums


if __name__ == "__main__":
    print(genSet([2, 3, 4, 1, 6, 4, 4, 1, 2]))
    print(genSet([-1, -3, -4, 8, 4, 2, -3, -1]))

__name__ = "__main__"
