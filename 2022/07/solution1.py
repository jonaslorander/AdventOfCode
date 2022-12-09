from collections import defaultdict
commands = open("input.txt").read().split("\n")

current_path = ["ROOT"]
directories = defaultdict(int)
ls_mode = False

for command in commands:
    cmd = command.split(" ")
    if cmd[0] == "$":
        if cmd[1] == "cd":
            ls_mode = False
            if cmd[2] == "..":
                current_path.pop()
            else:
                current_path.append(cmd[2])

        elif cmd[1] == "ls":
            ls_mode = True

    elif ls_mode:
        if cmd[0].isdigit():
            # Add sum to this folder, and all above
            for i in range(len(current_path)):
                directories["/".join(current_path[:i + 1])] += int(cmd[0])

print(sum([i if i <= 100000 else 0 for i in directories.values()]))