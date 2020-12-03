lines = open("input.txt").read().splitlines()

TREE = '#'
OPEN = '.'

MOVES = [
    [1, 1],
    [3, 1],
    [5, 1], 
    [7, 1],
    [1, 2]
]

WIDTH = len(lines[0]) - 1
HEIGHT = len(lines) - 1

def count_trees(move_right, move_down):
    x = move_right
    y = move_down
    trees = 0

    while y <= HEIGHT:
        if x > WIDTH:
            x = x - WIDTH - 1

        if lines[y][x] == TREE:
            trees = trees + 1

        x = x + move_right
        y = y + move_down
    
    return trees

tree_product = 1
for m in MOVES:
    ct = count_trees(m[0], m[1])
    print(f"Trees: {ct}")
    tree_product = tree_product * ct

print(f"Tree product: {tree_product}")