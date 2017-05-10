"""BA1_ba1b: Frequent Words Problem
Find the most frequent k-mers in a string.
Given: A DNA string Text and an integer k.
Return: All most frequent k-mers in Text (in any order)"""

import os
path=os.getcwd()

from BA1_ba1a import PatternCount

def CountDict(Text, k):
    """Generates a dictionary that counts kmers of length k where key = kmer string[index], value = kmer string count"""
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

def remove_duplicates(Items):
    """Removes duplicates from a list"""
    ItemsNoDuplicates=[]
    for i in Items:
        if i not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(i)
    return ItemsNoDuplicates

def FrequentWords(Text, k):
    """Generates a list of max frequency kmers of length k"""
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

# with open (path + r'/input_data/rosalind_ba1b.txt') as f:
#     input=f.read().strip().split('\n')
#     ba1b_text=input[0]
#     ba1b_k=int(input[1])
#
# f = open(path + r'/output_data/out-rosalind_ba1b.txt', 'w')
# f.write(str(' '.join(FrequentWords(ba1b_text,ba1b_k))))
# f.close()
#
# print((FrequentWords(ba1b_text,ba1b_k)))

def TopHits(Text, k,n):
    """Generates a dictionary that modifies FrequentWords to return kmers of length k within frequency max-n, where key = kmer string, value = frequency"""
    FrequentPatterns = {}
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] >= m-n:
            y=Text[i:i+k]
            FrequentPatterns[y]=Count[i]
    return FrequentPatterns

# print((TopHits(ba1b_text,ba1b_k,0)))
