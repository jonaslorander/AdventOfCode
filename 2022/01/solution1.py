elves = open("input.txt").read().split("\n\n")

calories = 0
for elf in elves:
    foods = elf.split("\n")
    elf_cal = 0
    for food in foods:
        elf_cal = elf_cal + int(food)

    calories = max(calories, elf_cal)

print(calories)
