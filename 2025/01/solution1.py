turns = open("input.txt").read().replace("L", "-").replace("R", "+").splitlines()

sum = 50
zeroes = 0

for turn in turns:
    turn = int(turn)
    sum = sum + (int(turn) % (100 if turn >= 0 else -100))

    if sum > 99:
        sum = sum - 100
    
    if sum < 0:
        sum = sum + 100


    if sum == 0:
        zeroes = zeroes + 1

print(zeroes)
