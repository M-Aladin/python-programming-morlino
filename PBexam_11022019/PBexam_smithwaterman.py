"""
Programming for Bioinformatics exam -- 11-02-2019
Python implementation of Smith-Waterman alignment algorithm
"""


def prettyprint(listoflists):
    """Input -> list of lists; print to screen in a legible format"""
    for row in listoflists:
        print(row)


def subst(a, b, subst_matrix):
    """
    Usage: first two arguments are single characters; third argument is a dictionary of dictionaries.
    Return substitution score of the characters
    """
    subst_score = subst_matrix[a][b]
    return subst_score


def findmax(scdiag, scleft, scup):
    """
    The arguments are scores (integers or floating-point numbers).
    Return a tuple containing the best score in the first position and the corresponding traceback
    direction in the second position.
    """
    scores = [scdiag, scleft, scup, 0]
    directions = ["diag", "left", "_up_", "STOP"]
    tup_list = list(zip(scores, directions))  # match each score with the corresponding direction
    tup_max = max(tup_list)  # the maximum is identified solely considering the 1st element of the tuple
    return tup_max


def smithwaterman(seqA, seqB, subst_matrix, gap_penalty):
    """
    The first two arguments are the sequences to align; the third argument is a dictionary of dictionaries; the fourth
    argument is an integer or floating-point number for gap penalty.
    Create two matrices given the sequence lengths and fill them according to the SW algorithm.
    Return values: score matrix, traceback matrix, imax and jmax (coordinates of best-scoring cell)
    """
    rows = len(seqA)
    cols = len(seqB)

    # matrix creation and initialization
    scorematrix = [[0 for col in range(cols)] for row in range(rows)]
    traceback = [["STOP" for col in range(cols)] for row in range(rows)]
    # coordinate pointer initialization (for traceback)
    imax = 0
    jmax = 0

    # iteration
    for i in range(1, rows):          # leave 1st row unchanged
        for j in range(1, cols):      # leave 1st column unchanged
            # compute the three possible extension scores
            diag_score = scorematrix[i-1][j-1] + subst(seqA[i], seqB[j], subst_matrix)
            left_score = scorematrix[i][j-1] + gap_penalty
            up_score = scorematrix[i-1][j] + gap_penalty
            # find and store the maximum score and corresponding direction
            maxresults = findmax(diag_score, left_score, up_score)
            scorematrix[i][j], traceback[i][j] = maxresults

            # keep track of best score found, and save its coordinates
            # update indices imax and jmax if new best score is found
            if scorematrix[i][j] >= scorematrix[imax][jmax]:
                imax = i
                jmax = j
    return scorematrix, traceback, imax, jmax


#############

# add an additional 0 to the beginning of the sequences, in order to have the same index number as the matrices
sequenceA = "".join(["0", "ATTACAGATCGAGATTACATTACGCGTAGCT"])
sequenceB = "".join(["0", "GATTACA"])

substitution = {"A": {"A": 2, "C": -1, "G": 0, "T": -1},
                "C": {"A": -1, "C": 2, "G": -1, "T": 0},
                "G": {"A": 0, "C": -1, "G": 2, "T": -1},
                "T": {"A": -1, "C": 0, "G": -1, "T": 2}}

gap = -1

results = smithwaterman(sequenceA, sequenceB, substitution, gap)

swscores, swtraceback, maxrow, maxcol = results

# output generation
print("Score matrix:")
prettyprint(swscores)
print("Traceback matrix:")
prettyprint(swtraceback)
print("Alignment score: {0}\nScore coordinates: {1}, {2}".format(swscores[maxrow][maxcol], maxrow, maxcol))
