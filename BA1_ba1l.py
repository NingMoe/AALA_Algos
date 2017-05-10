"""Convert a DNA string to a number.
Given: A DNA string Pattern.
Return: PatternToNumber(Pattern)."""

import os
path=os.getcwd()

def patterntonumber(string):
    """Converts a string into a unique number that represents the lexicographic index that would be assigned
    by a permutation list of strings of identical length"""
    tally=0
    for i in range(len(string)-1):
        number=0
        if string[i]=='A':
            number=0
        elif string[i]=='C':
            number=(1/4)*(4**(len(string)-i))
        elif string[i]=='G':
            number=(1/2)*(4**(len(string)-i))
        elif string[i]=='T':
            number=(3/4)*(4**(len(string)-i))
        tally+=number

    if string[-1]=='A':
        tally+=0
    elif string[-1]=='C':
        tally+=1
    elif string[-1]=='G':
        tally+=2
    elif string[-1]=='T':
        tally+=3

    return tally

# print (patterntonumber('CCCCGAT'))