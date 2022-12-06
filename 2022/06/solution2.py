indata = open("input.txt").read()

PREAMBLE_LENGTH = 14

sop = 0
for c in range((PREAMBLE_LENGTH - 1), len(indata)):
    test = indata[(c - (PREAMBLE_LENGTH - 1)):(c + 1)]
    for l in test:
        if test.count(l) > 1:
            sop = 0
            break

        sop = c + 1

    if sop > 0:
        break

print(sop)