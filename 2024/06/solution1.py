map_lines = open("input.txt").read().splitlines()
map_list = [list(line.strip()) for line in map_lines]
GUARD = ['^', '>', 'v', '<']
VISITED = 'X'
OBSTACLE = '#'

GuardDirection = {
    '^': [-1, 0],
    '>': [0, 1],
    'v': [1, 0],
    '<': [0, -1]
}

MAP_SIZE = (len(map_list), len(map_list[0]))

# Find guard starting position
guard = next(([y, x] for y, row in enumerate(map_list) for x, g in enumerate(row) if g in GUARD), None)

while True:
    gd = map_list[guard[0]][guard[1]]  # current Guard Direction
    d = GuardDirection[gd]  # guard direction coordinates difference
    map_list[guard[0]][guard[1]] = VISITED  # Mark current position as visited

    # Did the guard leave the map yet?
    if not (0 <= guard[0] + d[0] < MAP_SIZE[0]) and (0 <= guard[1] + d[1] < MAP_SIZE[0]):
        break

    # Check next position for obstacles
    next_gd = gd
    if map_list[guard[0] + d[0]][guard[1] + d[1]] == OBSTACLE:
        # Get the next direction from the dictionary
        dk = list(GuardDirection.keys())
        ci = dk.index(gd)
        next_gd = dk[(ci + 1) % 4]

    d = GuardDirection[next_gd]  # guard direction coordinates difference
    guard[0] = guard[0] + d[0]  # Next y coordinate
    guard[1] = guard[1] + d[1]  # Next x coordinate

    map_list[guard[0]][guard[1]] = next_gd

total_sum = sum(1 for _, row in enumerate(map_list) for _, value in enumerate(row) if value == VISITED)
print(total_sum)