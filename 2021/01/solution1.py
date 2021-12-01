depths = list(map(int, open("input.txt").read().splitlines()))

increase = 0

prev_depth = depths[0]
for depth in depths[1:]:
    if depth > prev_depth:
        increase = increase + 1

    prev_depth = depth

print(increase)
