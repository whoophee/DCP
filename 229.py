# This problem was asked by Flipkart.
# Snakes and Ladders is a game played on a 10 x 10 board, the goal of which is get from 
# square 1 to square 100. On each turn players will roll a six-sided die and move forward 
# a number of spaces equal to the result. If they land on a square that represents a snake 
# or ladder, they will be transported ahead or behind, respectively, to a new square.
# Find the smallest number of turns it takes to play snakes and ladders.
# For convenience, here are the squares representing snakes and ladders, and their outcomes:
# snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
# ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
####
def shortest_path(snakes, ladders, boardsize = 100, dice_rolls = [1, 2, 3, 4, 5, 6]):
    mappings = snakes
    mappings.update(ladders)

    moves = [(0,)]*(boardsize + max(dice_rolls) + 1)

    for i in range(0, boardsize):
        if i in mappings:
            continue
        cur_moves = moves[i]
        for j in dice_rolls:
            next_square = i+j
            next_square_aux = mappings.get(next_square, next_square)
            if len(moves[next_square]) == 1 or len(moves[next_square]) > len(cur_moves) + 1:
                nxt = (next_square, next_square_aux)
                if next_square == next_square_aux:
                    nxt = next_square
                moves[next_square_aux] = cur_moves + (nxt,)

    return moves[boardsize]
####
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
print(shortest_path(snakes, ladders))
