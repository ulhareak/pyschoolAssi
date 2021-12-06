
"""
In gene expression, mRNA is transcribed from a DNA template.
The 4 nucleotide bases of A, T, C, G corresponds to the U, A, G, C bases of the mRNA.
Write a function that returns the mRNA transcript given the sequence of a DNA strand.
Examples

    >>>mRNAtranscription("ATCGATTG")
    "UAGCUAAC"

"""
# Use a dictionary to provide the mapping of DNA to RNA bases.


def mRNAtranscription(dna_template):
    """Return mRNA transcript of DNA strand"""
    dna2rna = {
        "A": "U",
        "T": "A",
        "C": "G",
        "G": "C"}
    mRNA = ''
    for t in dna_template:
        if t in dna2rna.keys():
            mRNA += dna2rna[t]
        else:
            mRNA += t

    return mRNA

print(mRNAtranscription("ATCGATTG"))