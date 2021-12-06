
"""
A DNA strand consisting of the 4 nucleotide bases is usually represented with a string of
letters: A,T, C, G. Write a function that computes the base composition of a given DNA sequence.

Examples

    >>>baseComposition("CTATCGGCACCCTTTCAGCA")
    {'A': 4, 'C': 8, 'T': 5,  'G': 3 }
    >>>baseComposition("AGT")
    {'A': 1, 'C': 0, 'T': 1,  'G': 1 }
"""
def base_composition(dna_seq):
    """It computes base omposition of given DNA Seq."""
    d = {
        "A": 0,
        "C": 0,
        "T": 0,
        "G": 0}

    for i in d:
        d[i] = dna_seq.count(i)

    return d


print(base_composition("CTATCGGCACCCTTTCAGCA"))
print(base_composition("AGT"))
