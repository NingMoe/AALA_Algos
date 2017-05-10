"""Frequent Words with Mismatches Problem
Find the most frequent k-mers with mismatches in a string.
Given: A string Text as well as integers k and d.
Return: All most frequent k-mers with up to d mismatches in Text.
JSchendel has very different (and longer code) than me for the same result- is it faster?"""

import os
path=os.getcwd()

import itertools
from BA1_ba1h import ApproximatePatternMatching

def FrequentWords_Hamm(Text, k, d):
    """Probes every DNA nucleotide combination for substring length 'k' against string 'Text' with hamming distance =< 'd'. Returns a list of the most frequent substring even if that exact substring does not appear in string 'Text'."""
    comb_list=list(itertools.product('ACGT',repeat=k))
    flat_list=[]
    """flatten comb list into a list of strings"""
    for i in comb_list:
        x=''.join(i)
        flat_list.append(x)
    """progressively append or replace max count patterns in freq_patterns list"""
    max_count=1
    freq_patterns=[]
    for index, pattern in enumerate(flat_list):
        count=len(ApproximatePatternMatching(flat_list[index],Text,d))
        if count==max_count:
            freq_patterns.append(pattern)
        if count>max_count:
            max_count=count
            freq_patterns=[pattern]

    return freq_patterns

# with open (path + r'/input_data/rosalind_ba1i.txt') as f:
#     input=f.read().strip().split('\n')
#     text=input[0]
#     line2=input[1].split()
#     k=int(line2[0])
#     d=int(line2[1])
#
# f = open(path + r'/output_data/out_rosalind_ba1i.txt', 'w')
# f.write(' '.join(i for i in FrequentWords_Hamm(text,k,d)))
# f.close()
