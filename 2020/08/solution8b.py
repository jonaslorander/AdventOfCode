import copy

commands = open("input.txt").read().splitlines()

cmd = []
for command in commands:
    d = command.split(' ')
    cmd.append([d[0], int(d[1]), False]) # Command, parameter, visited

def run_cpu(cmd):
    acc = 0
    ptr = 0

    while ptr < len(cmd):
        c = cmd[ptr] # Get next command

        # Have we visited this command already?
        if c[2]:
            return [False, acc]

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

    return [True, acc]

for i in range(len(cmd)):
    cmd_copy = copy.deepcopy(cmd)

    if cmd_copy[i][0] == "jmp":
        cmd_copy[i][0] = "nop"

        result = run_cpu(cmd_copy)
        if result[0]:
            print(f"Program executed correctly, accumulator is {result[1]}, row {i}")
            break

print("End")