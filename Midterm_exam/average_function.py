# average_function.py
# For this exercise the pseudo-code is required (in this same file)
# Write a function that calculates the average of the values of
# any vector of 10 numbers
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average
# Define separate functions for the input and for calculating the average

"""
pseudo-code:

define INPUT FUNCTION:
- initialize list
- input number from keyboard
- append to list
- repeat previous two steps for a total of 10 times

define AVERAGE FUNCTION:
- sum all the numbers in the list
- divide by list length (in this case, we already know it's 10)

- call input function
- call average function passing the vector as an argument
- print the input and the average
"""


def vect10_input():
    """This function prompts the user to input 10 values from the keyboard and converts them into integers, returning
    a list containing all of them. If an invalid value is typed, the user is prompted to try again"""
    vect = []
    i = 0
    while i < 10:
        try:
            num = int(input("insert the %d° number:\n" % (i + 1)))
            vect.append(num)
            i = i + 1
        except ValueError:
            print("It seems that you typed an invalid value. Please try again")   # if the user messes up, the counter
            # doesn't increment, allowing for a retry. In this way, we end up with a 10-dimensional vector of integers
    return vect


def avg(v):     # potentially taking as arguments vectors of any length
    """This function takes a list of integers and returns the average value"""
    average = sum(v)/len(v)
    return average


V = vect10_input()
mean = avg(V)

print("The input vector is:\n{0}\n\nThe average value of the items is {1}".format(V, mean))
