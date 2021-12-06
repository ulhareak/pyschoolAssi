"""
Write a function invertDictionary(d) that takes in a dictionary as argument and return a
dictionary that inverts the keys and the values of the original dictionary.

Examples

    >>>invertDictionary({'a':1, 'b':2, 'c':3, 'd':2})
    {1: ['a'], 2: ['b', 'd'], 3: ['c']}
    >>>invertDictionary({'a':3, 'b':3, 'c':3})
    {3: ['a', 'c', 'b']}
    >>>invertDictionary({'a':2, 'b':1, 'c':2, 'd':1})
    {1: ['b', 'd'], 2: ['a', 'c']}
    """


def invert_dictionary(d):
    """it Returns inverted version of Dictinary"""
    keys = list(d.values())
    values = list(d.keys())
    dict2 = {}
    f_list=[]
    for keys, values in d.items():
        if values not in dict2.keys():
            dict2[values] = list(keys)
        else:
            f_list = list(dict2[values])
            f_list.append(keys)
            dict2[values] = f_list

    return dict2


print(invert_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 2}))
print(invert_dictionary({'a': 3, 'b': 3, 'c': 3}))
