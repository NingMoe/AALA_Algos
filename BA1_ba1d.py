"""PatternMatching Problem
Find all occurrences of a pattern in a string.
Given: Strings Pattern and Genome.
Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing."""

import os
path=os.getcwd()

def PatternMatching(Pattern, Genome):
    """Modifies PatternCount to return a list of starting index positions for each substring match in a string, where 'Pattern' = substring and 'Genome' = string"""
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
       if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

# with open (path + r'/input_data/rosalind_ba1d.txt') as f:
#     input=f.read().strip().split('\n')
#     ba1d_pattern=input[0]
#     ba1d_genome=input[1]
#
# f = open(path + r'/output_data/out_rosalind_ba1d.txt', 'w')
# f.write(' '.join(str(i) for i in PatternMatching(ba1d_pattern,ba1d_genome)))
# f.close()
