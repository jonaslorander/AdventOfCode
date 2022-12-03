bags = open("input.txt").read().split("\n")

sum = 0
for i in range(0, len(bags), 3):
    elves = [set(bags[i]), set(bags[i + 1]), set(bags[i + 2])]

    badge = (elves[0].intersection(elves[1], elves[2])).pop()

    badge_value = (ord(badge) - ord('a') + 1) if ord(badge) >= ord('a') else (ord(badge) - ord('A') + 27)
    sum = sum + badge_value

print(sum)