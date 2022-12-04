sections = open("input.txt").read().split("\n")

def range_subset(range1, range2):
    if range1.start >= range2.start and range1.stop <= range2.stop:
        return True
    else:
        return False

contained = 0
for pair in sections:
    sect_12 = pair.split(",")
    sect_1 = [int(i) for i in sect_12[0].split("-")]
    sect_2 = [int(i) for i in sect_12[1].split("-")]

    range_1 = range(sect_1[0], sect_1[1])
    range_2 = range(sect_2[0], sect_2[1])

    if range_subset(range_1, range_2) or range_subset(range_2, range_1):
        contained = contained + 1

print(contained)