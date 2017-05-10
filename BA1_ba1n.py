"""Generate the d-Neighborhood of a String
Find all the neighbors of a pattern.
Given: A DNA string Pattern and an integer d.
Return: The collection of strings Neighbors(Pattern, d)."""

import os
path=os.getcwd()

import itertools

string='ACGT'
string_list=list('ACGT')
string_index=[]

print(string_list)

for index, nucleotide in enumerate(string):
    string_index.append(index)

replacements=list(itertools.product('ACGT',repeat=2))
print(replacements)

index_combo=list(itertools.combinations(string_index,2))
print(index_combo)

combo_len=len(index_combo[0])
print(combo_len)
neighbours=[]



for x in index_combo:
    kmer = string_list
    for y in range(combo_len):
        m=x[y]
        for n in replacements:
            kmer[m]=n[y]
            print(kmer)

# print(replacements)

# for index in ham_index_combo:
#     string_list[ham_index_combo[index]]=sub_combo[index]
#     print (''.join(string_list))

