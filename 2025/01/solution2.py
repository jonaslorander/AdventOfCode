turns = open("input.txt").read().replace("L", "-").replace("R", "+").splitlines()

sum = 50
prev_sum = sum
zeroes = 0

for turn in turns:
    turn = int(turn)
    print(f"{sum}+ {turn} = {sum + turn} ", end='')
    sum = sum + turn

    if prev_sum == 0 and sum < 0:
        sum = sum + 100
        while sum < 0:
            sum = sum + 100
            zeroes = zeroes + 1
            print(" +0 ", end='')
        prev_sum = sum
        print(sum)
        continue
    
    while sum > 100:
        sum = sum - 100
        zeroes = zeroes + 1
        print(" +0 ", end='')
    
    while sum < 0:
        sum = sum + 100
        zeroes = zeroes + 1
        print(" +0 ", end='')

    if sum == 0 or sum == 100:
        sum = 0
        zeroes = zeroes + 1
        print(" +0+ ", end='')

    prev_sum = sum
    print(sum)

print(zeroes)