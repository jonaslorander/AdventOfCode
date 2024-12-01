rows = open("input.txt").read().splitlines()

total_differance = 0
list_left = []
list_right = []

for row in rows:
    distances = row.split("   ")
    list_left.append(int(distances[0]))

    list_right.append(int(distances[1]))

for i in range(len(list_left)):
    occurances = list_right.count(list_left[i])
    total_differance = total_differance + (list_left[i] * occurances)


print(total_differance)
