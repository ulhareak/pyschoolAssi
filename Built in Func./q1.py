"""
# Write a function that returns 4 lists given a postive number."""
def createLists(num):
    """retuns list of lists ."""
    l1 = l2 = l3 = l4 = []
    l1 = [x for x in range(1, num+1)]
    l2 = [x for x in range(num, 0, -1)]
    # l1.extend(l2)
    l3 = [-x for x in range(1, num+1)]
    l4 = [-x for x in range(num, 0, -1)]
    return (l1, l2, l4, l3)

if __name__=="__main__":
    print(createLists(5))
    print(createLists(4))
    