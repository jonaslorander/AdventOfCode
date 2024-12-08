karta = [list(line) for line in open("input.txt").read().splitlines()]

ANTINODE = '#'
MAP_SIZE = [len(karta), len(karta[0])]  # Coordinates are reversed, (Y; X)
ANTINODES = [['.' for _ in range(MAP_SIZE[0])] for _ in range(MAP_SIZE[1])]
ANTENNAS = {}

# Find all antennas and save their coordinates in a dictionary by type
for y, row in enumerate(karta):
    for x, v in enumerate(row):
        if v.isalnum():
            if not v in ANTENNAS:
                ANTENNAS[v] = []

            ANTENNAS[v].append((y, x))

# Loop through all antenna types and find their distances
#  Distances are needed to see if a node is outside of the map
for at in ANTENNAS:  # at = Antenna Type
    for i, _ in enumerate(ANTENNAS[at]):
        a1 = ANTENNAS[at][i]
        for a2 in ANTENNAS[at][i+1:]:
            dy = a2[0] - a1[0]
            dx = a2[1] - a1[1]

            # Check if antenna 1 and 2 plus difference is inside map and place an ANTINODE
            an1 = (a1[0] + dy, a1[1] + dx)
            an2 = (a2[0] - dy, a2[1] - dx)
            while (0 <= an1[0] < MAP_SIZE[0] and 0 <= an1[1] < MAP_SIZE[1]):
                karta[an1[0]][an1[1]] = ANTINODE
                ANTINODES[an1[0]][an1[1]] = ANTINODE
                an1 = (an1[0] + dy, an1[1] + dx)
                    
            while (0 <= an2[0] < MAP_SIZE[0] and 0 <= an2[1] < MAP_SIZE[1]):
                karta[an2[0]][an2[1]] = ANTINODE
                ANTINODES[an2[0]][an2[1]] = ANTINODE
                an2 = (an2[0] - dy, an2[1] - dx)

"""
for row in karta:
    print("".join(row))
print()
for row in ANTINODES:
    print("".join(row))
"""

antinode_sum = sum(1 for row in ANTINODES for coord in row if coord == ANTINODE)
print(f"Number of antinodes: {antinode_sum}")

