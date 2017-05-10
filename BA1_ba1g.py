"""Hamming Distance Problem
Compute the Hamming distance between two DNA strings.
Given: Two DNA strings.
Return: An integer value representing the Hamming distance."""

import os
path=os.getcwd()

def HammingDistance(p,q):
    """Returns an integer for the Hamming Distance separating string sequence 'p' and string sequence 'q'"""
    HamDist=0
    for i in range(0,len(p)):
        if p[i] is not q[i]:
            HamDist+=1
    return HamDist

# with open (path + r'/input_data/rosalind_ba1g.txt') as f:
#     input=f.read().strip().split('\n')
#     p_genome=input[0]
#     q_genome=input[1]
#
# f = open(path + r'/output_data/out_rosalind_ba1g.txt', 'w')
# f.write(str(HammingDistance(p_genome,q_genome)))
# f.close()

