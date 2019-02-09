"""
Viterbi algorithm implementation for hmms
Main difference from forward: instead of summing over the probabilities of the possible paths, we only consider the most
probable "step" in the path.

INPUT:
Model parameters (check forward_hmm.py pseudocode)
Sequence to evaluate

OUTPUT:
Most probable path
Probability of the sequence and path given the model


Setup
Define transition probabilities (dictionary of dictionaries)
Define emission probabilities (dictionary of dictionaries)
Define set of states
Define sequence
Create matrix (list of lists) for storing probabilities:
no. of rows = length of state list;
no. of columns = length of seq + 2
Create pointer matrix for storing pointers, same dimensions

Initialization
first column of the matrix => first element of each item in list of lists
probability of begin is 1 and probability of other states is 0
second column of the matrix => second element of each item in list of lists
In each cell, compute the product of probability of transition (B->current state) times probability of emission of
character 1.
In the corresponding cells in pointer matrix, set pointers to Begin

Iteration
For each column (i):
    For each cell in the column:
        Find the highest probability in the previous column and its corresponding state
        Store the state in the pointer matrix
        Multiply the probability to transition probability to current state and to emission probability of symbol (i)

Termination
Compile last column of the probability matrix: only the last cell is considered
Find the highest probability and its corresponding state in the previous column
Store the state in the pointer matrix
Multiply the probability to transition probability to end state
Store the final probability

Traceback
The aim is to reconstruct the sequence of states
Create empty list
Check bottom-right cell
Append state to list
Decrement column index
Row index varies based on the state indicated in the pointer. A dictionary maps indices and states.
While backtracing:
    Check cell indicated by the previous pointer
    Append state to list
    Decrement column index
    Row index varies based on the state indicated in the pointer
Reverse list
Join elements into single string

Generate output:
print probability of path, sequence given model
print path (maybe also aligned to sequence)
"""


def prettymatrix(listoflists):
    """Human-readable display of lists of lists"""
    for lyst in listoflists:
        print(lyst)


def seqdecorate(seq):
    """Index fixing of strings via appending 0's before and after"""
    dec = ["0", seq, "0"]
    decseq = "".join(dec)  # stands for "decorated sequence" but also for "decent sequence"
    return decseq


def findmax(probs, states):
    """This function takes as input a list of states and a list of scores, and returns a tuple where the
    0th item is the highest probability and the 1st item is the traceback pointer for the state"""
    tup = list(zip(probs, states))
    scmax = max(tup)
    return scmax


# set of states
state = {0: "B", 1: "Y", 2: "N", 3: "E"}

# transition probabilities -> dictionary of dictionaries
t = {"Y": {"Y": 0.7, "N": 0.2},
     "N": {"N": 0.8, "Y": 0.1}}  # usage: first key is starting state, second key is ending state

# starting and ending probabilities
begin = {"Y": 0.2, "N": 0.8}
end = {"Y": 0.1, "N": 0.1}

# emission probabilities -> dictionary of dictionaries
e = {"Y": {"A": 0.1, "C": 0.4, "G": 0.4, "T": 0.1},
     "N": {"A": 0.25, "C": 0.25, "G": 0.25, "T": 0.25}}

sequence = seqdecorate("ATGCG")

rows = len(state)
cols = len(sequence)

V = [[0 for col in range(cols)] for row in range(rows)]
T = [["Z" for kol in range(cols)] for rov in range(rows)]  # Z is some sort of "null" pointer


# initialization

V[0][0] = 1  # first cell

# second column
for i in range(1, rows-1):
    V[i][1] = begin[state[i]] * e[state[i]][sequence[1]]
    T[i][1] = "B"

# prettymatrix(V)
# prettymatrix(T)
# initialization block OK


# iteration

for j in range(2, cols-1):  # accessing columns
    for i in range(1, rows-1):  # accessing single elements in column j
        probabilities = []
        pointers = []
        for h in range(1, rows - 1):  # accessing single elements in column j-1 to find the max prob and pointers
            prob_app = V[h][j-1] * t[state[h]][state[i]] * e[state[i]][sequence[j]]
            probabilities.append(prob_app)
            pointers.append(state[h])
        V[i][j], T[i][j] = findmax(probabilities, pointers)

prettymatrix(V)
prettymatrix(T)

# termination block still to write
# probability check not ok, the calculus goes wrong somewhere
# pointer check ok
