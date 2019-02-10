"""
Needleman-Wunsch alignment algorithm

########

INPUT:
sequences to align
scoring matrix
gap penalties

OUTPUT:
alignment
score

########

Setup:
Define substitution and gap scores/penalties
Read input sequences
Add a 0 to the left of each sequence
no. rows = length of seq A
no. cols = length of seq B
Create score matrix filled with 0
Create traceback matrix filled with "null"

Initialization:
Top-left cell is 0
First row -> incrementation of gap penalties
First column -> incrementation of gap penalties

Iteration:
For each row (starting from second):
    for each cell in the row (starting from second):
        Compute the three scores leading to the cell
        Each score is coupled with its direction (tuple)
        Find max score and store it in the score matrix
        Find corresponding direction and store it in the traceback matrix

Termination:
Create two empty lists to store the alignments
Start from bottom-right cell in traceback matrix (define list containing the indices)
While a "null" cell is not reached in the traceback matrix:
    Check value in traceback matrix:
        Diag -> append to both lists the corresponding character, decrement both indices
        Left -> append gap to 1st sequence, character to 2nd sequence, decrement 2nd index
        Up -> append character to 2nd sequence, gap to 1st sequence, decrement 1st index
Reverse and join lists into strings

Generate output:
print alignment
print score
"""


def prettymatrix(listoflists):
    """Human-readable display of lists of lists"""
    for lyst in listoflists:
        print(lyst)


def findmax_nw(x, y, z):
    """
    Read three scores
    Zip them to list of directions
    Return the best score-direction tuple
    """
    directions = ["diag", "left", "_up_"]
    scores = [x, y, z]
    tup = list(zip(scores, directions))
    scmax = max(tup)
    return scmax


def subst(a, b, mat, mismat):
    """
    Read character a, character b, (strings) match score, mismatch penalty (integers)
    If a and be are equal, return the match score
    Otherwise, return the match penalty
    """
    if a == b:
        sc = mat
    elif a != b:
        sc = mismat

    return sc


def seqdecorate(seq):
    """Add a 0 at the beginning of the string 'seq'"""
    decseq = "".join(["0", seq])
    return decseq


# setup

# scores
match = 2
mismatch = -1
gap = -2

# sequences
seqA = seqdecorate("ACCA")
seqB = seqdecorate("ACTGG")

# matrices
rows = len(seqA)
cols = len(seqB)

NW = [[0 for col in range(cols)] for row in range(rows)]
traceback = [["null" for kol in range(cols)] for rov in range(rows)]

# initialization
for j in range(1, cols):  # populate first row
    NW[0][j] = NW[0][j-1] + gap
    traceback[0][j] = "left"
for i in range(1, rows):  # populate first column
    NW[i][0] = NW[i-1][0] + gap
    traceback[i][0] = "_up_"

# initialization check ok

# iteration
for i in range(1, rows):
    for j in range(1, cols):
        scdiag = NW[i-1][j-1] + subst(seqA[i], seqB[j], match, mismatch)
        scleft = NW[i][j-1] + gap
        scup = NW[i-1][j] + gap
        NW[i][j], traceback[i][j] = findmax_nw(scdiag, scleft, scup)

# iteration block ok

# traceback
listali1 = []
listali2 = []

ind = [rows-1, cols-1]

while traceback[ind[0]][ind[1]] != "null":
    if traceback[ind[0]][ind[1]] == "diag":
        listali1.append(seqA[ind[0]])
        listali2.append(seqB[ind[1]])
        ind[0] -= 1
        ind[1] -= 1
    elif traceback[ind[0]][ind[1]] == "left":
        listali1.append("-")
        listali2.append(seqB[ind[1]])
        ind[1] -= 1
    elif traceback[ind[0]][ind[1]] == "_up_":
        listali1.append(seqA[ind[0]])
        listali2.append("-")
        ind[0] -= 1

# output generation
score = NW[rows-1][cols-1]
ali1 = "".join(listali1[::-1])
ali2 = "".join(listali2[::-1])


print("%s\n%s"%(ali1, ali2))
print("score: %d"%score)
