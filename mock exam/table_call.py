# input value n from the keyboard and print the times table of that number

import formatting

num = int(input("Type an integer number:\n"))

tablah = formatting.times_table(num)

formatting.print_table(tablah, num)
