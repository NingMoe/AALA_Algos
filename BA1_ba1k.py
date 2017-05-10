"""Computing a Frequency Array
Generate the frequency array of a DNA string.
Given: A DNA string Text and an integer k.
Return: The frequency array of k-mers in Text."""

import os
path=os.getcwd()

import itertools
from BA1_ba1a import PatternCount

def pattern_list(k):
    """Generate a list of ACGT combinations of length 'k' for use in frequency arrays"""
    p_list=[]
    for i in list(itertools.product('ACGT', repeat=k)):
        x = ''.join(i)
        p_list.append(x)
    return p_list

def frequency_array(text, k):
    """Generate a count list for each possible 'ACGT' pattern of length k in string 'text'. List index matches the pattern list."""
    freq_list=[]
    p_list=pattern_list(k)
    for i in p_list:
        freq_list.append(PatternCount(i,text))
    return freq_list

# with open (path + r'/input_data/rosalind_ba1k.txt') as f:
#     input=f.read().strip().split('\n')
#     text=input[0]
#     k=int(input[1])
#
# f = open(path + r'/output_data/out_rosalind_ba1k.txt', 'w')
# f.write(' '.join(str(i) for i in frequency_array(text,k)))
# f.close()
