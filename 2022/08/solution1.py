trees_input = open("input.txt").read().splitlines()

trees = []
for row in trees_input:
    tree_row = []
    for tree in row:
        tree_row.append((int(tree), False))
    trees.append(tree_row)

# Check rows first from left
for r in range(len(trees)):
    highest_tree = -1
    for t in range(len(trees[r])):
        h = trees[r][t][0]

        if h > highest_tree:
            trees[r][t] = (h, True)

        highest_tree = max(highest_tree, h)

# Check rows from right
for r in range(len(trees)):
    highest_tree = -1
    for t in range(len(trees[r]))[::-1]:
        h = trees[r][t][0]

        if h > highest_tree:
            trees[r][t] = (h, True)

        highest_tree = max(highest_tree, h)

# Transpose matrix
trees = [[trees[j][i] for j in range(len(trees))] for i in range(len(trees[0]))]

# Check rows first from top
for r in range(len(trees)):
    highest_tree = -1
    for t in range(len(trees[r])):
        h = trees[r][t][0]
        if h > highest_tree:
            trees[r][t] = (h, True)

        highest_tree = max(highest_tree, h)

# Check columns from bottom
for r in range(len(trees)):
    highest_tree = -1
    for t in range(len(trees[r]))[::-1]:
        h = trees[r][t][0]

        if h > highest_tree:
            trees[r][t] = (h, True)

        highest_tree = max(highest_tree, h)

"""
trees = [[trees[j][i] for j in range(len(trees))] for i in range(len(trees[0]))]
for row in trees:
    print(row)
"""

print(sum([True for row in trees for tree in row if tree[1]]))