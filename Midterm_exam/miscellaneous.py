# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3

L = list(range(21, 40))
print("Input:\n", L, "\n")

# since I know the numbers in my list I can do the following:

L_even = L[1::2]  # take one number every two starting from the second position
print("Evens:", L_even)
L_three = L[::3]  # since the first element is multiple of 3, start from the first position and pick one element every 3
print("Multiples of three:", L_three, "\n")

# generalization, given any list of consecutive integers

if L[0] % 2 == 0:   # decide where to start slicing
    print("Evens:", L[::2])
else:               # if the first element is odd, start slicing from second position
    print("Evens:", L[1::2])  # always slice list with step = 2

if L[0] % 3 == 0:       # if and elif statements decide where to slice based on the modulus of the first item
    print("Multiples of three:", L[::3])
elif L[0] % 3 == 2:
    print("Multiples of three:", L[1::3])
elif L[0] % 3 == 1:
    print("Multiples of three:", L[2::3])

print("\n")   # spacing out the output lines so they all can be checked in a single run

# Exercise 2
# Print the last two elements of L

print("last two elements:\n{0:8d}{1:8d}".format(L[-2], L[-1]))
print("\n\n")

# Exercise 3
# What's wrong with the following piece of code? Fix it and
# modify the code in order to have it work AND to have "<i> is in the list"
# printed at least once

# L = ['1', '2', '3']           -> this is a list of characters
# for i in range(10)            -> range(10) returns an immutable sequence of integers! Also, missing columns
#     if i in L:                -> the boolean expression will always be False
#     print(i is in the list)   -> quotation marks are missing in both print statements
#     else:
#     print(i not found)        -> indentation is missing in both branches of the if construct

# correct code:

L = ['1', '2', '3']
for i in range(10):    # taking the same interval of integers
    char = str(i)      # convert each item in a character and store in temporary variable
    if char in L:      # will be true for i values 1, 2, 3
        print("%s is in the list" % char)
    else:
        print("%s not found" % char)

print("\n")

# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list

fasta = open("sprot_prot.fasta")
line1 = fasta.readline()
splitted = line1.split("OS=")

print(splitted[1].rstrip())


# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string
fields = splitted[1].split()    # method splits by whitespace by default
species = "{0} {1}".format(fields[0], fields[1])   # concatenation by neat formatting
print(species, "\n")

# Exercise 6
# reverse the string 'asor rosa'

roses = "asor rosa"
sesor = roses[::-1]
print("Looking at the code, you can clearly acknowledge that {0} and {1} are palindromes\n".format(roses, sesor))

# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]

L = [1, 7, 3, 9]
print("At first I was like\n", L)
L.sort()                           # sort doesn't return anything, it directly changes the original list
print("But then I was like\n", L)

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L

L = [1, 7, 3, 9]
L1 = L.copy()            # storing a copy somewhere else, so I can sort it and keep the original
L1.sort()
print("Original list:\n{0}\nSorted list:\n{1}".format(L, L1))

# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6

table = [[2, 4], [3, 6]]               # prepare input as list of lists
with open('Table.txt', 'w') as fyle:   # ensure file closing if exceptions are raised
    fyle.write("{0}\t{1}\n{2}\t{3}".format(table[0][0], table[0][1], table[1][0], table[1][1]))
print("Check the file Table.txt")
