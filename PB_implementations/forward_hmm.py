"""
Forward algorithm implementation for hmms.

INPUT:
- model parameters
    set of states
    transition probabilities
    starting probabilities
    ending probabilities
    probabilities of emission of each character from each state
- sequence to evaluate

OUTPUT: probability of sequence given model


Setup
Define transition probabilities (dictionary of dictionaries)
Define emission probabilities (dictionary of dictionaries)
Define set of states
Define sequence
Create matrix (list of lists) for storing probabilities:
no. of rows = length of state list;
no. of columns = length of seq + 2

Initialization
first column of the matrix => first element of each item in list of lists
probability of begin is 1 and probability of other states is 0
the first row (begin state) is always filled with 0, so is the last row (end state)
second column of the matrix => second element of each item in list of lists
for each cell of the column, compute a sum:
each term of the sum is composed of the value of a cell in the previous column, times the transition probability
from the state of that cell to the state of the cell we are considering, times the emission probability
Do the same with all the i^th columns of the matrix until the last one

Termination
Last column of the matrix => last element of each item in list of lists
Probability of transitions is 0 except for end state
The only cell that needs to be computed is the bottom right cell, containing the sums of the previous scores times
the respective transition probabilities to end state

Generate output
Retrieve value of bottom right cell
print "the probability of this sequence given the model is..." (value)
"""


def prettymatrix(listoflists):
    """Human-readable display of lists of lists"""
    for lyst in listoflists:
        print(lyst)


def seqdecorate(seq):
    """index fixing of strings via appending 0's before and after"""
    dec = ["0", seq, "0"]
    decseq = "".join(dec)
    return decseq


# set of states
state = {0: "B", 1: "Y", 2: "N", 3: "E"}

# transition probabilities -> dictionary of dictionaries
t = {"Y": {"Y": 0.7, "N": 0.2},
     "N": {"N": 0.8, "Y": 0.1}}  # transitions are as follows: first key is starting state, second key is ending state

# starting and ending probabilities
begin = {"Y": 0.2, "N": 0.8}
end = {"Y": 0.1, "N": 0.1}

# emission probabilities -> dictionary of dictionaries
e = {"Y": {"A": 0.1, "C": 0.4, "G": 0.4, "T": 0.1},
     "N": {"A": 0.25, "C": 0.25, "G": 0.25, "T": 0.25}}

sequence = seqdecorate("ATGCG")

rows = len(state)
cols = len(sequence) # there is no need to put a +2 because we decorated it, adjusting its length

F = [[0 for col in range(cols)] for row in range(rows)]
# row/col check OK


# initialization

F[0][0] = 1  # begin state has probability 1 in the first column

# population of second column
for i in range(1, rows-1):
    F[i][1] = begin[state[i]] * e[state[i]][sequence[1]]
# prettymatrix(F)
# initialization block ok

# iteration: population of whole matrix until last column

for j in range(2, cols-1):  # identifies the columns to traverse (except for already populated first 2 columns)
    print("#"*10)
    print("col", j)
    for i in range(1, rows-1):  # traverses the columns, except for first and last cell (begin and end states)
        print('*'*5)
        print("row", i)
        for h in range(1, rows-1):
            # this for cycle traverses the previous column for every cell of the current column
            F[i][j] += F[h][j-1] * t[state[h]][state[i]] * e[state[i]][sequence[j]]
            print(F[i][j], F[h][j-1], t[state[h]][state[i]], e[state[i]][sequence[j]], sequence[j])

# prettymatrix(F)
# iteration block almost ok
#

# termination

for i in range(1, rows-1):  # traversing the last column excluding first and last cell
    F[rows-1][cols-1] += F[i][cols-2] * end[state[i]]   # the -1 are necessary because we defined matrix length using
    # the range function

print(F[rows-1][cols-1])
