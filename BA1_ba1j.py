"""Frequent Words with Mismatches and Reverse Complements Problem
Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.
Given: A DNA string Text as well as integers k and d.
Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers."""

import os
path=os.getcwd()

import itertools

from BA1_ba1h import ApproximatePatternMatching
from BA1_ba1c import ReverseComplementDNA

def FrequentWords_Hamm_rev(Text, k, d):
    comb_list=list(itertools.product('ACGT',repeat=k))
    flat_list=[]

    for i in comb_list:
        x=''.join(i)
        flat_list.append(x)

    max_count=1
    freq_patterns=[]
    for index, pattern in enumerate(flat_list):
        fwd_count=len(ApproximatePatternMatching(flat_list[index],Text,d))
        rev_count=len(ApproximatePatternMatching(flat_list[index],ReverseComplementDNA(Text),d))
        count=fwd_count+rev_count
        if count==max_count:
            freq_patterns.append(pattern)
        if count>max_count:
            max_count=count
            freq_patterns=[pattern]

    return freq_patterns

# with open (path + r'/input_data/rosalind_ba1j.txt') as f:
#     input=f.read().strip().split('\n')
#     text=input[0]
#     line2=input[1].split()
#     k=int(line2[0])
#     d=int(line2[1])
#
# f = open(path + r'/output_data/out_rosalind_ba1j.txt', 'w')
# f.write(' '.join(i for i in FrequentWords_Hamm(text,k,d)))
# f.close()
#
