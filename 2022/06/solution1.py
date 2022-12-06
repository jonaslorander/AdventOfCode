indata = open("input.txt").read()

sop = 0
for c in range(3, len(indata)):
    test = indata[(c - 3):(c + 1)]
    for l in test:
        if test.count(l) > 1:
            sop = 0
            break

        sop = c + 1

    if sop > 0:
        break

print(sop)