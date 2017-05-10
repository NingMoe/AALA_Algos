"""BA1_ba1a: Implement PatternCount
Given: {DNA strings}} Text and Pattern.
Return: Count(Text, Pattern)."""

import os
path=os.getcwd()

def PatternCount(Pattern, Text):
    """Counts occurrence of a substring in string"""
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# with open (path + r'/input_data/rosalind_ba1a.txt') as f:
#     input=f.read().strip().split('\n')
#     ba1a_text=input[0]
#     ba1a_pattern=input[1]
#
# f = open(path + r'/output_data/out_rosalind_ba1a.txt', 'w')
# f.write(str(PatternCount(ba1a_pattern,ba1a_text)))
# f.close()
#
# print(PatternCount(ba1a_pattern,ba1a_text))

from BA1_ba1c import Reverse_Complement

def PatternCountPlusrevComp(Pattern, Text):
    """Modifies the PatternCount function to include the reverse complement of the given substring"""
    count = 0
    revComp=Reverse_Complement(Pattern)
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
        if Text[i:i+len(Pattern)] == revComp:
            count = count+1
    return count

# print(PatternCountPlusrevComp(ba1a_pattern,ba1a_text))
# print('hello world')

def occurrences(string, sub):
    "This code is pretty cool, but not sure if I understand it!"
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

