"""
Pairwise comparision of DNA sequences is a popular technique
used in Bioinformatics. It usually involves some scoring scheme
to express the degree of similarity. Write a function that compares
two DNA sequences based on
the following scoring scheme: +1 for a match, +3 for each
consecutive match and -1 for each mismatch.

Examples

    >>> print pairwiseScore("ATTCGT", "ATCTAT")
    ATTCGT
    ||   |
    ATCTAT
    Score: 2 
    >>> print pairwiseScore("GATAAATCTGGTCT", "CATTCATCATGCAA")
    GATAAATCTGGTCT
     ||  |||  |   
    CATTCATCATGCAA
    Score: 4 
    >>>
"""


def pairwiseScore(seqA, seqB):
    """" returns Priewise comp. of DNA seq. """
    score = 0
    f = False
    s = ""

    for i in range(len(seqA)):
        if seqA[i] == seqB[i]:
            s += "|"
            if f == True:
                score += 3
                continue
            score += 1
            f = True
        else:
            s += " "
            f = False
            score -= 1

    return "{}\n{}\n{}\nScore: {}".format(seqA, s, seqB, score)


def main():
	"""Works as a main function of a program"""
    print(pairwiseScore("GATAAATCTGGTCT", "CATTCATCATGCAA"))
    print(pairwiseScore("ATTCGT", "ATCTAT"))
    print("added new line ")


if __name__ + + "__main__":
    main()
