"""Implement NumberToPattern
Convert an integer to its corresponding DNA string.
Given: Integers index and k.
Return: NumberToPattern(index, k)."""

import os
path=os.getcwd()

def numbertosymbol(number):
    """Converts numbers 0,1,2,3 to nucleotides ACGT respectively."""
    if number==0:
        n='A'
    elif number==1:
        n='C'
    elif number==2:
        n='G'
    elif number==3:
        n='T'
    return n

def numbertopattern(index,k):
    """Returns a DNA string after converting an index value 'index' from a lexicographic ACGT
    permutation list. A string length must also be given 'k'"""
    pattern=[]
    quotient=index
    while quotient>=4:
        modulo = divmod(quotient, 4)
        quotient = modulo[0]
        remainder = modulo[1]
        pattern.append(numbertosymbol(remainder))
    else:
        pattern.append(numbertosymbol(quotient))
    if k>len(pattern):
        x=k-len(pattern)
        pattern.append(('A')*x)

    return ''.join(pattern[::-1])

