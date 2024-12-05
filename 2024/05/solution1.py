rules, pages = open("input.txt").read().split("\n\n")

pages = pages.splitlines()
rules = rules.splitlines()

total_sum = 0

print("Validating input...")
for line in pages:
    valids = []
    for rule in rules:
        p1, p2 = rule.split("|")

        lp = line.split(",")  # Line pages
        if not (p1 in lp and p2 in lp):
            continue

        i = lp.index(p1)

        if i:
            valids.append(p2 in lp[i:])

    if all(valids):
        median = int(line.split(",")[len(line.split(",")) // 2])
        total_sum += median

print(f"Sum is {total_sum}.")