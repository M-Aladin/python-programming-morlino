"""
Backward algorithm implementation for hmms

###########

INPUT:
model parameters
sequence to evaluate

OUTPUT:
probability of sequence given model

###########

Setup
Read list of states
Read transition probabilities
Read emission probabilities
Read sequence
rows = n. of states
cols = length of sequence
Create a rows x cols matrix

Initialization
Start from last column of matrix
Store in each cell of the column the corresponding transition from that state to the end state

Iteration
For each column (proceeding backwards):
    For each cell in column:
        sum over the probabilities of the following column, times the transition probabilities to that column,
        times the emission probabilities of the "following" symbol

Termination
Compute total score by summing over the probabilities in the first column, times the transition
probabilities to the first column, times the emission probabilities of the 1st symbol in each state

Generate output: print probability
"""


def prettymatrix(listoflists):
    """Human-readable display of lists of lists"""
    for lyst in listoflists:
        print(lyst)


# set of states
state = ["B", "Y", "N", "E"]

# transition probabilities -> dictionary of dictionaries
t = {"B": {"B": 0, "Y": 0.2, "N": 0.8, "E": 0},
     "Y": {"B": 0, "Y": 0.7, "N": 0.2, "E": 0.1},
     "N": {"B": 0, "N": 0.8, "Y": 0.1, "E": 0.1},
     "E": {"B": 0, "N": 0, "Y": 0, "E": 0}}
# transitions are used as follows: first key is starting state, second key is ending state

# starting and ending probabilities
begin = {"Y": 0.2, "N": 0.8}
end = {"Y": 0.1, "N": 0.1}  # usage ex.: end["Y"] is the trans probability from Yes to End

# emission probabilities -> dictionary of dictionaries
e = {"Y": {"A": 0.1, "C": 0.4, "G": 0.4, "T": 0.1},
     "N": {"A": 0.25, "C": 0.25, "G": 0.25, "T": 0.25}}

# input sequence
sequence = "ATGCG"

# matrix setup
rows = len(state)
cols = len(sequence)
backward = [[0 for col in range(cols)] for row in range(rows)]

# initialization
for i in range(1, rows-1):
    backward[i][cols-1] = end[state[i]]

# iteration
for j in range(cols-2, -1, -1):
    for i in range(1, rows-1):
        for h in range(1, rows-1):
            increment = backward[h][j+1] * t[state[i]][state[h]] * e[state[h]][sequence[j+1]]
            backward[i][j] += increment

# termination
score = 0
for h in range(1, rows-1):
    increment = backward[h][0] * begin[state[h]]
    score += increment

prettymatrix(backward)
print(score)

# output: 0.00035011440000000003
