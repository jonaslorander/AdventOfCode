sections = open("input.txt").read().split("\n")

isect = 0
for pair in sections:
    sect_12 = pair.split(",")
    sect_1 = [int(i) for i in sect_12[0].split("-")]
    sect_2 = [int(i) for i in sect_12[1].split("-")]

    range_1 = [i for i in range(sect_1[0], sect_1[1] + 1)]
    range_2 = [i for i in range(sect_2[0], sect_2[1] + 1)]

    if any(e in range_2 for e in range_1) or any(e in range_1 for e in range_2):
        isect = isect + 1

print(isect)