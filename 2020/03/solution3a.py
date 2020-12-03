lines = open("input.txt").read().splitlines()

TREE = '#'
OPEN = '.'
HIT = 'X'
MISS = 'O'

MOVE_RIGHT = 3
MOVE_DOWN = 1

WIDTH = len(lines[0]) - 1
HEIGHT = len(lines) - 1

x = MOVE_RIGHT
y = MOVE_DOWN
trees = 0

print(WIDTH, HEIGHT)

while y <= HEIGHT:
    if x > WIDTH:
        x = x - WIDTH - 1

    l = list(lines[y])
    if lines[y][x] == TREE:
        l[x] = HIT
        trees = trees + 1
    else:
        l[x] = MISS

    lines[y] = "".join(l)

    print(f"{x:3};{y:3}: {lines[y]} - {lines[y][x]}")

    x = x + MOVE_RIGHT
    y = y + MOVE_DOWN

print(f"Trees: {trees}")