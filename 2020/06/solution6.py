groups = open("input.txt").read().split("\n\n")

# Part 1
def group_answers(g):
    yes = "".join(set(g))
    return len(yes)

# Part 2
def group_all_answers(g):
    persons = g.count("\n") + 1 # No new line after last person
    g = g.replace("\n", "")
    yes = {i : g.count(i) for i in set(g)} 
    all_yes = [k for k,v in yes.items() if v == persons]
    return len(all_yes)

# Part 1
total_yes = 0
for group in groups:
    total_yes += group_answers(group.replace("\n", ""))

print(f"Total yes: {total_yes}")

# Part 2
total_yes = 0
for group in groups:
    total_yes += group_all_answers(group.rstrip("\n"))

print(f"Total yes: {total_yes}")