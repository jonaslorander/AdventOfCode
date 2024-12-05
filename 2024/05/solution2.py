rules, pages = open("input.txt").read().split("\n\n")

pages = pages.splitlines()
rules = rules.splitlines()

total_sum = 0

def apply_rules(lp):   
    valid = True 
    for rule in rules:
        p1, p2 = rule.split("|")

        if not (p1 in lp and p2 in lp):
            continue

        i1 = lp.index(p1)
        i2 = lp.index(p2)

        if p2 not in lp[i1:]:
            lp[i1], lp[i2] = lp[i2], lp[i1]
            lp, valid = apply_rules(lp)
            valid = False

    return lp, valid

print("Validating input...")
for line in pages:
    invalids = []
    valid = True
    lp = line.split(",")  # Line pages

    lp, valid = apply_rules(lp)

    if not valid:
        total_sum += int(lp[len(lp) // 2])

print(f"Sum is {total_sum}.")