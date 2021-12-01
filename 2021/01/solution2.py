depths = list(map(int, open("input.txt").read().splitlines()))

increase = 0
win = 3

i = 0
sums = []
for i in range(len(depths) - win + 1):
    sums.append(sum(depths[i:i + win]))

prev_depth = sums[0]
for depth in sums[1:]:
    if depth > prev_depth:
        increase = increase + 1

    prev_depth = depth

print(increase)