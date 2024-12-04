
Directions = {
    1: [0, 0, ["M", "S"]],
    2: [2, 0, ["M", "S"]],
    3: [1, 1, ["A", "A"]],
    4: [0, 2, ["M", "S"]],
    5: [2, 2, ["M", "S"]],
}

class MapTraverser():
    def __init__(self):
        pass

    def load(self, data):
        self.map = data
        self.width = len(self.map[0]) - 1
        self.height = len(self.map) - 1
        self.result = 0

    # Go thourgh coordinates by coordinate
    def find_xmas(self):
        for y in range(self.height + 1):
            for x in range(self.width + 1):
                if self.map[y][x] in ["M", "S"] and x <= self.width - 2 and y <= self.height - 2:
                    found = True
                    for d in Directions:
                        #print(f"({y};{x})({self.map[y][x]}), ({y + Directions[d][1]};{x + Directions[d][0]})({self.map[y + Directions[d][1]][x + Directions[d][0]]}), {Directions[d][2]}, {self.map[y + Directions[d][1]][x + Directions[d][0]] in Directions[d][2]}")
                        if not ( \
                            (self.map[y + Directions[d][1]][x + Directions[d][0]] in Directions[d][2]) and \
                            (self.map[y + Directions[1][1]][x + Directions[1][0]] != self.map[y + Directions[5][1]][x + Directions[5][0]]) and \
                            (self.map[y + Directions[2][1]][x + Directions[2][0]] != self.map[y + Directions[4][1]][x + Directions[4][0]])):
                            found = False
                            break
                    
                    if found:
                        self.result += 1

        return self.result

map_lines = open("input.txt").read().splitlines()
map_list = [list(line.strip()) for line in map_lines]

xmas = MapTraverser()
xmas.load(map_list)  # Load 2D map
print("Searching...")
total_xmas = xmas.find_xmas()  # Find string XMAS

print(f"Found {total_xmas} matches.")