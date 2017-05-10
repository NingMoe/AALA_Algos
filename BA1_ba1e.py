"""Clump Finding Problem
Find patterns forming clumps in a string.
Given: A string Genome, and integers k, L, and t.
Return: All distinct k-mers forming (L, t)-clumps in Genome."""

import os
path=os.getcwd()
from BA1_ba1b import TopHits
from BA1_ba1d import PatternMatching

def FrequentWords_clump(text, k, l):
    """Slow algorithm (slow): Generates a dictionary of lists for genome 'text' where keys = max frequency kmers of length 'k',
    values[0]=no. occurrences, values[1]=starting text[index] of windows length 'l'."""
    max_clumps={}
    """Create a dictionary of frequent kmers and their max occurrences in each sliding window"""
    for i in range(len(text)-l+1): #increase range step for faster processing (lower accuracy)
        freq_kmers=TopHits(text[i:i+l],k,0)
        for key, value in freq_kmers.items():
            if key in max_clumps.keys():
                if value > max_clumps[key][0]:
                    max_clumps[key]=(value,i)
            else:
                max_clumps[key] = (value, i)

    max_kmers={}
    """Rebuild the dictionary with only the most common kmers"""
    for keys,values in max_clumps.items():
        if values[0]==max((values[0] for values in max_clumps.values())):
            max_kmers[keys]=values

    return max_kmers

def FrequentWords_clump_ros(text,k,t,l):
    """Fast Algorithm: Returns a string of kmers of length 'k' that clump 't' times in any subtring of length 'l'
    in genome 'text'."""
    kmer_list=[]
    for i in range(len(text)-k+1):
        kmer=text[i:i+k]
        if kmer not in kmer_list:
            kmer_list.append(kmer)

    kmer_dict={}
    for x in kmer_list:
        kmer_dict[x]=PatternMatching(x,text)

    kmers=''
    for keys,values in kmer_dict.items():
        if CheckClumpLength(values,t,l) is True:
            kmers+=keys+' '

    return kmers

def CheckClumpLength(index,t,l):
    for i in range(len(index)-t+1):
        if index[t+i-1]-index[i]<=l:
            return True
    return False

# with open (path + r'/input_data/rosalind_ba1e.txt') as f:
#     input=f.read().strip().split('\n')
#     ba1e_text=input[0]
#     ba1e_klt=input[1].split()
#     ba1e_k=int(ba1e_klt[0])
#     ba1e_l=int(ba1e_klt[1])
#     ba1e_t=int(ba1e_klt[2])
#
# f = open(path + r'/output_data/out-rosalind_ba1e.txt', 'w')
# f.write(str(FrequentWords_clump_ros(ba1e_text,ba1e_k,ba1e_t,ba1e_l)))
# f.close()
