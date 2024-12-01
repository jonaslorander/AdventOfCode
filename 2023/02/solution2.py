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

sum_power = 0

for game in games:
    sum_power = sum_power + (game["red"] * game["green"] * game["blue"])

print(sum_power)