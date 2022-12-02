elves = open("input.txt").read().split("\n\n")

calories = []
for elf in elves:
    foods = elf.split("\n")
    elf_cal = 0
    for food in foods:
        elf_cal = elf_cal + int(food)

    calories.append(elf_cal)

calories.sort()

print(sum(calories[-3:]))
