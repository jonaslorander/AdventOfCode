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
    to_stack = to_stack - 1
    from_stack = from_stack - 1

    if len(stacks[from_stack]) == 0:
        return

    to_pop = min(len(stacks[from_stack]), crates)
    stacks[to_stack] = stacks[from_stack][:to_pop] + stacks[to_stack]
    stacks[from_stack] = stacks[from_stack][to_pop:]

# Move the crates around!
for move in moves:
    move = move.split(",")
    do_move(int(move[0]), int(move[1]), int(move[2]))

tops = ""
# Get top of all stacks
for stack in stacks:
    tops = tops + stack[0]

print(tops)
