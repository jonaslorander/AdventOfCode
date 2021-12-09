instructions = open("input.txt").read().splitlines()

forward = 0
depth = 0

for inst in instructions:
    if "forward" in inst:
        forward = forward + int(inst[-1])

    if "up" in inst:
        depth = depth - int(inst[-1])

    if "down" in inst:
        depth = depth + int(inst[-1])

print(f"{forward} * {depth} = {forward * depth}")