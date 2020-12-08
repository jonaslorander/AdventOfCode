commands = open("input.txt").read().splitlines()

acc = 0
ptr = 0
cmd = []
for command in commands:
    d = command.split(' ')
    cmd.append([d[0], int(d[1]), False]) # Command, parameter, visited

while ptr <= len(cmd):
    c = cmd[ptr] # Get next command

    # Have we visited this command already?
    if c[2]:
        break

    c[2] = True # Set visited flag
    if c[0] == "nop":
        ptr += 1
    elif c[0] == "acc":
        acc += c[1]
        ptr += 1
        if acc < 0:
            acc = 0
    elif c[0] == "jmp":
        ptr += c[1]
        if ptr < 0:
            ptr = 0

print(f"The value in the accumulator is {acc}")