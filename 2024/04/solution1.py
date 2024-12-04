from mp import MapTraverser, Directions

map_lines = open("input.txt").read().splitlines()
map_list = [list(line.strip()) for line in map_lines]

xmas = MapTraverser()
xmas.load(map_list)  # Load 2D map
print("Searching...")
total_xmas = xmas.find("XMAS")  # Find string XMAS

print(f"Found {total_xmas} matches.")