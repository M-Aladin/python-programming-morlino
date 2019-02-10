f = open("10_sequences.seq")

print("Input summary:")
i = 1
for seq in f:
    print(i, seq.rstrip())
    i = i+1

f.seek(0)
print("\n\n")

for seq in f:
    print(seq)
    if "A" in seq:
        print("A count: {0:3d}".format(seq.count("A")))
    else:
        print("A not found")

    if "T" in seq:
        print("T count: {0:3d}".format(seq.count("T")))
    else:
        print("T not found")

    if "C" in seq:
        print("C count: {0:3d}".format(seq.count("C")))
    else:
        print("C not found")

    if "G" in seq:
        print("G count: {0:3d}".format(seq.count("G")))
    else:
        print("G not found")

    print("\n")

f.seek(0)

i = 1
ind = []
print("Retrieving pattern CTATA")
for seq in f:
    if "CTATA" in seq:
        print(seq.rstrip())
        ind.append(i)
    i = i+1
print("first hit at sequence {0:1d}".format(ind[0]))
f.close()
