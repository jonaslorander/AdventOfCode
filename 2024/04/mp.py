
Directions = {
    "NW": (-1, -1),
    "N":  (0, -1),
    "NE": (1, -1),
    "E":  (1, 0),
    "SE": (1, 1),
    "S":  (0, 1),
    "SW": (-1, 1),
    "W":  (-1, 0)
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
    def find(self, search_string):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[x][y] == search_string[0]:
                    # Start a search from the same coordinate in all different directions
                    for d in Directions:
                        self.result += self.__find_direction(x, y, search_string, 0, d)

        return self.result
    
    def __find_direction(self, x, y, ss, c, d):  # x & y = coordinates, ss = search_string, c = character index, d = direction
        next_x = x + Directions[d][0]
        next_y = y + Directions[d][1]
        next_c = c + 1
        
        # Have we found the entire string?
        if next_c == len(ss):
            return 1
        # Check boundaries
        elif not ((0 <= next_x <= self.width) and (0 <= next_y <= self.height)):
            return 0
        # Check if we can continue to move in the same direction
        elif (next_x < 0 and d in ["NE", "E", "SE"]) or \
            ( next_x > self.width and d in ["NW", "W", "SW"]) or \
            ( next_y < 0 and d in ["NW", "N", "NE"]) or \
            ( next_y > self.height and d in ["SE", "S", "SW"]):
            return 0
        # Did we find the next character? If so continue in the same direction
        elif self.map[next_x][next_y] == ss[next_c]:
            return self.__find_direction(next_x, next_y, ss, next_c, d)
        else:
            return 0
        