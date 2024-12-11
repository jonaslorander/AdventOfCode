stones = open("input.txt").read().split()

def apply_rules(stone):
    if stone == 0:
        return [1]
    
    if not len(str(stone)) % 2:
        stone = str(stone)
        half_val = int(len(stone) / 2)
        return [int(stone[:half_val]), int(stone[half_val:])]
    
    return [stone * 2024]

for i in range(25):
    new_stones = [apply_rules(int(stone)) for stone in stones]
    stones = [stone for s in new_stones for stone in s]

print(f"Total stones after 25 blinks are: {len(stones)}")