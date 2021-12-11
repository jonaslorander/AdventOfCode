input = open("input.txt").read().splitlines()

def print_boards(boards):
    i = 0
    for board in boards:
        if i > 4:
            print()
            i = 0
            

        for row in board:
            print(row)
            i = i + 1

# Drawn numbers
numbers = list(map(int, input.pop(0).strip().split(",")))

# Get bingo boards
boards = []
while(len(input) > 5):
    input.pop(0)
    board = []
    for _ in range(5):
        board.append(list(map(int, input.pop(0).split())))

    boards.append(board)

# Start playing bing!
for n_idx, number in enumerate(numbers):
    for b_idx, board in enumerate(boards):
        for r_idx, row in enumerate(board):
            for c_idx, column in enumerate(row):
                if column == number:
                    boards[b_idx][r_idx][c_idx] = -number

    # Check for bingo
    bingo = True
    bingo_sum = 0

    # Check horisontal first  
    b = 0
    for b in range(len(boards)):
        r = 0
        for r in range(len(boards[b])):
            c = 0
            bingo = True
            for c in range(len(boards[b][r])):
                if boards[b][r][c] >= 0:
                    bingo = False
                    break

            if bingo:
                print(f"Bingo! {boards[b]}")
                break

        if bingo:
            board_sum = 0
            for row in boards[b]:
                for col in row:
                    if col >= 0:
                        bingo_sum = bingo_sum + col

            break

    # Then check vertical
    b = 0
    for b in range(len(boards)):
        r = 0
        for r in range(len(boards[b])):
            c = 0
            bingo = True
            for c in range(len(boards[b][r])):
                if boards[b][c][r] >= 0:
                    bingo = False
                    break

            if bingo:
                print(f"Bingo! {boards[b]}")
                break

        if bingo:
            board_sum = 0
            for row in boards[b]:
                for col in row:
                    if col >= 0:
                        bingo_sum = bingo_sum + col

            break
    
    if bingo:
        print(bingo_sum, (bingo_sum * number))
        break
