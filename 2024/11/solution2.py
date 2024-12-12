from math import log10
import time

start = time.time()
stones = open("input.txt").read().split()
stones = [int(stone) for stone in stones]

BLINKS = 75

def apply_rules(stone):
    if stone == 0:
        return (1,)
    
    num_digits = int(log10(stone)) + 1
    if num_digits % 2 == 0:
        divisor = 10 ** (num_digits // 2)
        return (stone // divisor, stone % divisor)
    
    return (stone * 2024,)

STONES = {}
for stone in stones:
    STONES[stone] = 1

for i in range(BLINKS):
    S = {}
    for stone in STONES:
        if STONES[stone] > 0:
            val = apply_rules(stone)
            if len(val) == 2:
                if val[1] in S:
                    S[val[1]] += STONES[stone]
                else:
                    S[val[1]] = STONES[stone]

            if val[0] in S:
                S[val[0]] += STONES[stone]
            else:
                S[val[0]] = STONES[stone]
    STONES = S.copy()

STONE_LEN = sum([STONES[s] for s in STONES])
stop = time.time()
print(f"Total stones after {BLINKS} blinks are: {STONE_LEN}. It took {stop - start} seconds.")