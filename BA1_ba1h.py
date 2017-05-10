"""Approximate Pattern Matching Problem
Find all approximate occurrences of a pattern in a string.
Given: Strings Pattern and Text along with an integer d.
Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches."""

import os
path=os.getcwd()

from BA1_ba1g import HammingDistance

def ApproximatePatternMatching(Pattern, Text, d):
    """Returns a list of index positions for the appearance of substring 'Pattern' in string 'Text' within mismatch tolerance range 'd' (Hamming Distance)"""
    positions = []
    for i in range(len(Text) - len(Pattern) + 1):
        x=Pattern
        y = Text[i:i + len(Pattern)]
        if HammingDistance(x,y)<=d:
            positions.append(i)
    return positions

# with open (path + r'/input_data/rosalind_ba1h.txt') as f:
#     input=f.read().strip().split('\n')
#     pattern=input[0]
#     text=input[1]
#     hamm=int(input[2])
#
# f = open(path + r'/output_data/out_rosalind_ba1h.txt', 'w')
# f.write(' '.join(str(i) for i in ApproximatePatternMatching(pattern,text,hamm)))
# f.close()
