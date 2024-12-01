rows = open("input.txt").read().splitlines()

games = []

for row in rows:
    gs = {"red": 0, "green": 0, "blue": 0}  # gs = max know cubes per color holder
    game = row.replace("Game ", "").split(":")  # split game into game number and sets
    s = game[1].split(";")  # split sets
    #print(f"Game {game[0]}")

    for ss in s:  # ss = split sets
        #print(ss)
        c = ss.split(",")  # split color
        #print(c)
        for cubes in c:
            cc = cubes.strip().split(" ")  # cubes per color

            if int(cc[0]) > gs[cc[1]]:
                gs[cc[1]] = int(cc[0])

    #print(gs)
    games.append(gs)

#print(games)

elf = {}
elf["red"] = 12
elf["green"] = 13
elf["blue"] = 14

sum_id = 0

for i in range(len(rows)):
    game = dict(games[i])
    #print(i + 1, game)
    if not (game["red"] > elf["red"] or game["green"] > elf["green"] or game["blue"] > elf["blue"]):
        sum_id = sum_id + (i + 1)

print(sum_id)