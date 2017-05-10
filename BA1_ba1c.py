"""BA1_ba1c: Reverse Complement Problem
Find the reverse complement of a DNA string.
Given: A DNA string Pattern.
Return: Pattern, the reverse complement of Pattern."""

import os
path=os.getcwd()

def Reverse_Complement(Pattern):
    """Generates a reverse complement string, with my own functions, from DNA string 'nucleotide'"""
    revComp=complement(Pattern[::-1])
    return revComp

def complement(Nucleotide):
    """Generates a complement string from DNA string 'nucleotide'"""
    comp=''
    for i in Nucleotide:
        if i=='A':
            comp+='T'
        elif i=='T':
            comp += 'A'
        elif i=='G':
            comp += 'C'
        elif i=='C':
            comp += 'G'
        else:
            comp += 'n'
    return comp

# with open (path + r'/input_data/rosalind_ba1c.txt') as f:
#     input=f.read().strip().split('\n')
#     ba1c_text=input[0]
#
# f = open(path + r'/output_data/out-rosalind_ba1c.txt', 'w')
# f.write(Reverse_Complement(ba1c_text))
# f.close()
#
# print(Reverse_Complement(ba1c_text))

"""BA1_ba1c: Can also be solved with Biopython Seq"""
from Bio import Seq as seq

# print(seq.reverse_complement(ba1c_text))

def ReverseComplementDNA(nucleic_acid):
    """Generates a reverse complement string, using string.maketrans method, from DNA string 'nucleic_acid'"""
    nucleotide = 'ATCG'
    complement = 'TAGC'
    transtab = nucleic_acid.maketrans(nucleotide, complement)
    return nucleic_acid.translate(transtab)[::-1].lstrip()

# print(ReverseComplementDNA(ba1c_text))



