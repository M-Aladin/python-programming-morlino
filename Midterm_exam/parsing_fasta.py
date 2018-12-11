# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file)
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence length
# Use separate functions for the input and the output


"""
Pseudo-code:

define ORGANISM PARSING FUNCTION:
- split line by "OS="
- split second element of the list obtained above by whitespace
- concatenate first two elements of the newly obtained list
- return the name of the organism

define HEADER PARSING FUNCTION:
- if the line starts with > then it's a header


- open the file with the sequences
- open another file for writing later

- run through all the lines
- if the line is a header, store it in list1 and append a space to list2
- if the line is not a header, store it in list2

- at the end, build a list where each element is the n^th sequence

- for each header in the list header:
    - parse the source organism
    - if it's not homo sapiens, retrieve sequence with the same index in the sequence list
"""


def parse_organism(line):
    l1 = line.split("OS=")
    l2 = l1[1].split()
    species_list = [l2[0], l2[1]]
    org = " ".join(species_list)
    return org


def isheader(line):
    if line.startswith('>'):
        return True
    else:
        return False


f = open("sprot_prot.fasta")    # open the input file
output = open("non_human_seq.fasta", 'w')   # open the output file
seq_list = []       # initialize lists
head_list = []

for line in f:
    if isheader(line):          # if the line is a header, append it to a list and append a space to the list of seqs
        head_list.append(line.rstrip())
        seq_list.append(" ")
    else:                       # if the line is not a header, it's a sequence, so append to the seq list
        seq_list.append(line.rstrip())

seq_string = "".join(seq_list)  # make a ginormous string out of the sequence lines list
sequences = seq_string.split()  # split by space (works because when we found a header we appended a " " item)

# at this point, we have: one list with all the headers (head_list) and one list with all the sequences (sequences)

for head in head_list:
    organism = parse_organism(head)
    if organism != "Homo sapiens":
        i = head_list.index(head)
        output.write("{0}\n{1}\n".format(head_list[i], sequences[i]))  # the index of each header is equal
        # to the index of the corresponding sequence
        print(organism)
        print(len(sequences[i]))

# close all files for safety
f.close()
output.close()
