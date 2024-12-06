map_lines = open("input.txt").read().splitlines()
map_list = [list(line.strip()) for line in map_lines]
GUARD = ['^', '>', 'v', '<']
VISITED = 'X'
OBSTACLE = '#'
NEW_OBSTACLE = 'O'
OBSTACLES = [OBSTACLE, NEW_OBSTACLE]
LOOP = ['+', '-', '|']

GuardDirection = {
    '^': [-1, 0],
    '>': [0, 1],
    'v': [1, 0],
    '<': [0, -1]
}

MAP_SIZE = (len(map_list), len(map_list[0]))

# Find guard starting position
guard = next(([y, x] for y, row in enumerate(map_list) for x, g in enumerate(row) if g in GUARD), None)

def find_loop():
    global guard, GUARD, GuardDirection, map_list
    visits = [[0 for _ in range(MAP_SIZE[0])] for _ in range(MAP_SIZE[1])]

    g = list(guard)
    gd = map_list[g[0]][g[1]]  # current Guard Direction, should update

    while True:
        d = GuardDirection[gd]  # guard direction coordinates difference
        visits[g[0]][g[1]] += 1  # Increase visits

        # Check if we have visited the same place more than X times, then we surely are in a loop...?
        if visits[g[0]][g[1]] > 10:
            return True

        # Did the guard leave the map, then we did not find a loop
        if not ((0 <= g[0] + d[0] < MAP_SIZE[0]) and (0 <= g[1] + d[1] < MAP_SIZE[1])):
            return False

        # Check next position for obstacles
        if map_list[g[0] + d[0]][g[1] + d[1]] in OBSTACLES:
            # Get the next direction from the dictionary
            dk = list(GuardDirection.keys())
            ci = dk.index(gd)
            gd = dk[(ci + 1) % 4]
            dt = GuardDirection[gd]
            temp = [g[0] + dt[0], g[1] + dt[1]]
            # Check again
            if map_list[temp[0]][temp[1]] in OBSTACLES:
                # Get the next direction from the dictionary
                dk = list(GuardDirection.keys())
                ci = dk.index(gd)
                gd = dk[(ci + 1) % 4]

        d = GuardDirection[gd]  # guard direction coordinates difference
        g[0] = g[0] + d[0]  # Next y coordinate
        g[1] = g[1] + d[1]  # Next x coordinate

total_loops = 0
for y, row in enumerate(map_list):
    for x, value in enumerate(row):
        if map_list[y][x] not in GUARD + [OBSTACLE]:
            map_list[y][x] = NEW_OBSTACLE
            if find_loop():
                total_loops += 1
            map_list[y][x] = '.'

print(total_loops)