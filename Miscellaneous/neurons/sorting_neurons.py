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

fl1 = []
fl2 = []

for i in l1:
    fl1.append(float(i))
for i in l2:
    fl2.append(float(i))

avg1 = sum(fl1)/len(fl1)
avg2 = sum(fl2)/len(fl2)

print("--Average values of dendritic neuron length--\nPrimary neurons: {0:4.2f}\nSecondary neurons: {1:4.2f}".format(avg1, avg2))

# finish this with the standard deviation
