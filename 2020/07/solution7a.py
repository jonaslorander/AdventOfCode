rules = open("input.txt").read().replace(" bags", "").replace(" bag", "").split(".\n")

# Clean up the input
rules_dict = {}
for rule in rules:
    if len(rule) > 0:
        r = rule.split(" contain ")
        rules_dict[r[0]] = [k[2:].strip() for k in r[1].split(", ")]

# recursive function to find all posible bags a specified color can be contained
def find_all_posible_bags(color):
    posible_bags = []

    for k,v in rules_dict.items():
        if color in v and not (color in posible_bags):
            posible_bags.append(k)

    if len(posible_bags) > 0:
        for bag in posible_bags:
            more_bags = find_all_posible_bags(bag)
            if len(more_bags) > 0:
                posible_bags += [b for b in more_bags if not b in posible_bags ]

    return posible_bags

print(f"Shiny gold bags can be found in {len(find_all_posible_bags('shiny gold'))} bags.")
