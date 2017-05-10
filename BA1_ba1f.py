"""Minimum Skew Problem
Find a position in a genome minimizing the skew.
Given: A DNA string Genome.
Return: All integer(s) i minimizing Skew(Prefix(Text)) over all values of i (from 0 to |Genome|)."""

import os
path=os.getcwd()

def Skew(Genome):
    """Generates a dictionary of indexes with a running total whereby C and G are replaced with -1 or +1 respectively as a sequence is read"""
    skew={}
    n=len(Genome)
    skew[0]=0
    for i in range(1,(n+1)):
        skew[i]=skew[i-1]
        if Genome[i-1] == 'G':
            skew[i]=skew[i]+1
        elif Genome[i-1] == 'C':
            skew[i]=skew[i]-1
        else:
            skew[i]=skew[i]
    return skew

def MinimumSkew(Genome):
    """Returns a list containing the Genome[index] for minimum skew. This position represents the candidate ori position for a genome"""
    positions=[]
    SkewMap=Skew(Genome)
    n=min(SkewMap.values())
    for i in SkewMap:
        if SkewMap[i]==n:
            positions.append(i)
    return positions

def MaximumSkew(Genome):
    """Returns a list containing the Genome[index] for minimum skew. This position represents the candidate ori position for a genome"""
    positions=[]
    SkewMap=Skew(Genome)
    n=max(SkewMap.values())
    for i in SkewMap:
        if SkewMap[i]==n:
            positions.append(i)
    return positions

# with open (path + r'/input_data/rosalind_ba1f.txt') as f:
#     input=f.read().strip().split('\n')
#     ba1f_genome=input[0]
#
# f = open(path + r'/output_data/out_rosalind_ba1f.txt', 'w')
# f.write(' '.join(str(i) for i in MinimumSkew(ba1f_genome)))
# f.close()

def minimum_skew(genome):
    """JSchendel: Revised function for MinimumSkew involving progressive replacement of the minimum skew as iteration proceeds through 'genome."""
    skew_value=0
    min_skew=1
    min_skew_ind=[]
    """create a skew value at each index as it is iterated"""
    for index, nucleotide in enumerate(genome):
        if nucleotide == 'C':
            skew_value += -1
        elif nucleotide == 'G':
            skew_value += 1
        """append or replace minimum skew results in list"""
        if skew_value == min_skew:
            """append: min_skew is added to existing list"""
            min_skew_ind.append(str(index+1))
        elif skew_value < min_skew:
            """replace: (min_skew is reassigned, min_skew_ind is replaced)"""
            min_skew = skew_value
            min_skew_ind = [str(index+1)]

    return min_skew_ind
