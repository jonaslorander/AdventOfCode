xmap = open("input.txt").read().splitlines()

Directions = {
    'N': [-1, 0],
    'E': [0, 1],
    'S': [1, 0],
    'W': [0, -1]
}

def get_opposite(dir):
    vect = Directions[dir]
    opposite_vect = [-vect[0], -vect[1]]
    for dir, vec in Directions.items():
        if vec == opposite_vect:
            return dir

class Position():
    def __init__(self, y, x, h):
        self.y = y
        self.x = x
        self.h = h
        self.entry = "U"

    def __repr__(self):
        return f"|({self.y};{self.x})-{self.h}-{self.entry}|"

xmap = [[Position(y, x, int(h)) for x, h in enumerate(row)] for y, row in enumerate(xmap)]
MAP_SIZE = [len(xmap), len(xmap[0])]

def find_neighbours(m, pos):
    neighbours = []
    for dir in Directions:
        if pos.entry != dir:
            if  0 <= (pos.y + Directions[dir][0]) < MAP_SIZE[0] and \
                0 <= (pos.x + Directions[dir][1]) < MAP_SIZE[1] and \
                (m[pos.y + Directions[dir][0]][pos.x + Directions[dir][1]].h - pos.h == 1):
                neighbour = m[pos.y + Directions[dir][0]][pos.x + Directions[dir][1]]
                neighbour.entry = get_opposite(dir)
                neighbours.append(neighbour)

    return neighbours

total_paths = 0
def dfs(m, start, visited=None):
    global total_paths
    if visited is None:
        visited = set()
    
    if start.h == 9:
        total_paths += 1
    visited.add(start)

    neighbours = find_neighbours(m, start)
    if neighbours:
        for neighbour in neighbours:
            if neighbour not in visited:
                dfs(m, neighbour, visited)

    return visited

[dfs(xmap, pos) for row in xmap for pos in row if pos.h == 0]
print(f"Total number of paths available: {total_paths}")

