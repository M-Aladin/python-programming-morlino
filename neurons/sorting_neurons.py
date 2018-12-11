f = open("neuron_data-2.txt")

l1 = []
l2 = []

for line in f:
    temp = line.split()
    if temp[0] == '1':
        l1.append(temp[1])
    elif temp[0] == '2':
        l2.append(temp[1])

print("Lengths of primary neurons:\n{0}\n\nLengths of secondary neurons:\n{1}".format(l1, l2))
