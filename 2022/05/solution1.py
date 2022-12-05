indata = open("input.txt").read().split("\n\n")

# Clean up stack data
crates = indata[0].replace("    \n", " [ ]\n").replace("    ", " [ ]").replace("] [", "").replace("[", "").replace("]", "").split("\n")
crates = crates[:-1]
print(crates)

# Build stacks from crates
stacks = [[], [], [], [], [], [], [], [], []]
for row, data in enumerate(crates):
    for i, c in enumerate(data):
        if c != " ":
            stacks[i].append(c)

print(stacks)

# Clean up move data
moves = indata[1].replace("move ", "").replace(" from ", ",").replace(" to ", ",")
moves = moves.split("\n")

# Function to move crates from one stack to another
def do_move(crates, from_stack, to_stack):
    while crates > 0 and len(stacks[from_stack - 1]) > 0:
        stacks[to_stack - 1].insert(0, stacks[from_stack - 1].pop(0))
        crates = crates - 1

# Move the crates around!
for move in moves:
    move = move.split(",")
    do_move(int(move[0]), int(move[1]), int(move[2]))

tops = ""
# Get top of all stacks
for stack in stacks:
    tops = tops + stack.pop(0)

print(tops)
