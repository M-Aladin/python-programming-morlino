"""input -> read from file
output -> write to new file"""

from Miscellaneous.snek import rot13

input = open('ROT13')
output = open('ROT13_decoded', 'w')

for line in input:
    output.write(rot13(line))
