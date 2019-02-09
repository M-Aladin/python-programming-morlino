"""
Implementation of an algorithm to define a scoring matrix given a set of sequence alignments without gaps

INPUT:
alignments

OUTPUT:
scoring matrix

Read alignments as list of lists of sequences
Count and store all occurrences of each character; count total length; divide each value in dictionary for total length
Zip the alignments, count and store all occurrences of each possible tuple considering that, for example, (A,G) and
(G,A) should increment the same counter
Map each tuple to its p(i,j)/(p(i)*p(j)) value, considering that inverse tuples should map to same value
Transform this last dictionary in a matrix (list of lists), by using YET ANOTHER dictionary that maps ACGT to 0123,
in order to define the positions of the list in which each value should be stored
"""


aligns = [["ACAGGTGGACCT", "ACTGGTCGACTT"], ["CTATATGG", "CCGGATCG"]]
zip_ali = []

p_i = dict()
tot_len = 0
subs_redundant = dict()

for align in aligns:
    zip_ali.append(list(zip(align[0], align[1])))  # build lists of tuples for later
    for seq in align:
        tot_len += len(seq)
        for char in seq:
            if char not in p_i:
                p_i[char] = 1
            else:
                p_i[char] += 1

# print(p_i)
# print(tot_len)
# first check ok
# print(zip_ali)
# zip ok

for key in p_i:
    p_i[key] = p_i[key]/tot_len

# value modification, the dictionary now maps each letter i to its a priori probability p(i)

# we can actually start zipping already in the first for cycle (which I did and checked if it worked, see above)
# we have zipped seqs stored in the list of tuples zip_ali

for align in zip_ali:
    for chara, charb in align:
        if (chara, charb) not in subs_redundant:
            subs_redundant[(chara, charb)] = 1
        else:
            subs_redundant[(chara, charb)] += 1

print(zip_ali)
print(subs_redundant)
