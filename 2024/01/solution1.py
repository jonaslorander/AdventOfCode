rows = open("input.txt").read().splitlines()

total_differance = 0
list_left = []
list_right = []

for row in rows:
    distances = row.split("   ")
    list_left.append(int(distances[0]))
    list_right.append(int(distances[1]))

list_left.sort()
list_right.sort()

for i in range(len(list_left)):
    total_differance = total_differance + abs(list_left[i] - list_right[i])


print(total_differance)
