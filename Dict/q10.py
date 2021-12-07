"""
A sparse vector is a vector whose entries are almost all zero,
like [1, 0, 0, 0, 0, 0, 0, 2, 0]. Storing all those zeros wastes memory and
dictionaries are commonly used to keep track of just the nonzero entries.
For example, the vector shown earlier can be represented as {0:1, 7:2}, since the
vector it is meant to represent has the value 1 at index 0 and the value 2 at index 7.
Write a function that converts a sparse vector into a dictionary as described above.

Examples

    >>>convertVector([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4])
    {0: 1, 3: 2, 7: 3, 12: 4}
    >>>convertVector([1, 0, 1 , 0, 2, 0, 1, 0, 0, 1, 0])
    {0: 1, 2: 1, 4: 2, 6: 1, 9: 1}
    >>>convertVector([0, 0, 0, 0, 0])
    {}
"""


def convert_vector(numbers):
    """Convert nubers into dictio. """
    d_final = {}
    for i in range(len(numbers)):
        if numbers[i] != 0:
            d_final[i] = numbers[i]
    return d_final


print(convert_vector([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4]))
print(convert_vector([1, 0, 1, 0, 2, 0, 1, 0, 0, 1, 0]))
