games = open("input.txt").read().split("\n")

HANDS = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS"
}

POINTS = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
    "LOSS": 0,
    "DRAW": 3,
    "WIN": 6
}

def RPS(a, b):
    if  a == b:
        return "DRAW"

    elif (a == "ROCK" and b == "SCISSORS") or (a == "SCISSORS" and b == "PAPER") or (a == "PAPER" and b == "ROCK"):
        return "WIN"

    else:
        return "LOSS"

my_points = 0

for game in games:
    hands = game.split(" ")
    elf = HANDS[hands[0]]
    me = HANDS[hands[1]]

    my_points = my_points + (POINTS[me] + POINTS[RPS(me, elf)])

print(my_points)
