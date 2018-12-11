# first function to define: times_table(n)
# it should return a table where 1st column is numbers i(1-10) and 2nd column is n*i


def times_table(n):
    table = []
    for i in range(1, 11):
        table.append([i, n*i])
    return table


# second function: takes a 2x2 table and prints it with nice formatting
# is t a list of lists? ---> yos, ideally


def print_table(t, n):
    for i in t:
        print("{0:4d}*{1:1d} {2:4d}".format(i[0], n, i[1]))
