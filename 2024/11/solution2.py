from functools import lru_cache
from math import log10
from diskcache import Cache

stones = open("input.txt").read().split()
stones = [int(stone) for stone in stones]
cache = Cache("./my_cache")

#@lru_cache(maxsize=1000000)
def apply_rules(stone):
    if stone in cache:
        return cache[stone]
    
    if stone == 0:
        return (1,)
    
    num_digits = int(log10(stone)) + 1
    if num_digits % 2 == 0:
        divisor = 10 ** (num_digits // 2)
        ret = (stone // divisor, stone % divisor)
        cache[stone] = ret
        return ret
    
    ret = (stone * 2024,)
    cache[stone] = ret
    return ret

for i in range(75):
    print(i)
    stones = (stone for s in (apply_rules(stone) for stone in stones) for stone in s)

stones = list(stones)
print(f"Total stones after 25 blinks are: {len(stones)}")