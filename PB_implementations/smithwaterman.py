"""
Smith-waterman alignment algorithm

INPUT: sequences, scoring matrix
OUTPUT: alignment, score

Setup:
Define gap penalties and substitution matrix
Given sequence lengths, create matrix of dimensions len+1 for scores
Create another matrix of same dimensions for directions (-> traceback)
Initialize variables for max index storing to 0


Initialization
first row and first col to zero (but for simplicity the matrix is created equal to zero)


Iteration
For each position F(i,j) in the matrix (excluding 0th row and 0th column):
compute the scores of the three possible extensions that lead to that alignment:
- F(i-1, j-1) + subst score (direction DIAG)
- F(i-1, j) + gap penalty (direction LEFT)
- F(i, j-1) + gap penalty (direction UP)

Make a list of (score, direction) tuples:
- 1st item diag
- 2nd item gap seq 1 (LEFT)
- 3rd item gap seq 2 (UP)
- 4th item zero (STOP)

Find the max of the tuples, the 0^th element of the max is assigned to the score matrix, the 1^st element of the max
is assigned to the traceback matrix.
Keep track of indexes for maximum values:
Every time the current score in the cycle is greater than the current max indexes values, update them to the current
pointers in the cycle.


Termination

Initialize two empty lists
Find the max among all the values in the scoring matrix with the previously saved indices
Check direction in the same cell of the traceback matrix
While the direction is != STOP:
Diag direction: decrement both indices, append to both sequences the corresponding indices
Up direction: decrement first index (up one row), append corresponding index to seq1 and gap to seq2
Left direction: decrement second index (left one column), append gap to seq1 and corresponding index to seq2
Reverse both lists
join each list into single string

generate output:
print the two strings one under the other
"alignment score is " + score
"""
# scores
# match = 2
# mismatch = -1
# gap = -1


def subst(a, b, mat, mismat):
    """This function takes two characters and returns an integer that adds up to a score for match or mismatch.
    Match and mismatch contributes are defined inside the function."""
    if a == b:
        sc = mat
    elif a != b:
        sc = mismat

    return sc


def scoring(x, y, z):

    """This function takes as input the three extension scores around a cell and returns a tuple where the
    0th item is the score of the optimal extension and the 1st item is the traceback direction of the extension"""

    directions = ["diag", "left", "_up_", "STOP"]
    scores = [x, y, z, 0]
    tup = list(zip(scores, directions))
    scmax = max(tup)
    return scmax


def prettymatrix(listoflists):
    """Human-readable display of lists of lists"""
    for lyst in listoflists:
        print(lyst)


seq1 = "0GATTACA"
seq2 = "0CCCCCCCAAAAAAAGATATACAAAAAAAAAATTTT"

imax = 0
jmax = 0
ali_score = 0

r = len(seq1)
c = len(seq2)

match = 2
mismatch = -1
gap = -2

# initialization of the matrix with c columns and r rows
# one matrix for the score and one for the traceback directions

score_matrix = [[0 for col in range(c)] for row in range(r)]
traceback = [['STOP' for kol in range(c)] for rov in range(r)]


# matrix completion


for i in range(1, r):
    for j in range(1, c):
        scdiag = score_matrix[i-1][j-1] + subst(seq1[i], seq2[j], match, mismatch)
        scleft = score_matrix[i][j-1] + gap
        scup = score_matrix[i-1][j] + gap
        maxres = scoring(scdiag, scleft, scup)
        score_matrix[i][j] = maxres[0]
        traceback[i][j] = maxres[1]

        if maxres[0] >= ali_score:   # this block updates max value and its coordinates
            ali_score = maxres[0]   # at the end of the cycles, it will yield the max value and its position.
            imax = i                # very useful for traceback
            jmax = j


prettymatrix(traceback)
prettymatrix(score_matrix)


# traceback

rev_ali1 = []
rev_ali2 = []

while traceback[imax][jmax] != "STOP":
    if traceback[imax][jmax] == "diag":
        rev_ali1.append(seq1[imax])
        rev_ali2.append(seq2[jmax])
        imax -= 1
        jmax -= 1
    elif traceback[imax][jmax] == "left":
        rev_ali1.append("-")
        rev_ali2.append(seq2[jmax])
        jmax -= 1
    elif traceback[imax][jmax] == "_up_":
        rev_ali1.append(seq1[imax])
        rev_ali2.append("-")
        imax -= 1

ali1 = "".join(rev_ali1[::-1])  # reverse and join both lists
ali2 = "".join(rev_ali2[::-1])


# output generation
print("{0}\n{1}".format(ali1, ali2))
print("score:", ali_score)

# next debugging steps: check indices, test alignment on some known sequences to compare results.
# there is some problem with indices and also with the scoring function
# bugs probably fixed
# modularize by defining traceback function? It can probably be done by declaring the empty lists as global in the
# function, so as not to pass them as arguments
