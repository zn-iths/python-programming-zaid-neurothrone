MAX_CHESS_SQUARES = 8 * 8

total_grains = 0
grains_in_square = 1

for _ in range(MAX_CHESS_SQUARES):
    total_grains += grains_in_square
    grains_in_square *= 2

print(f"Total grains in a 8x8 chessboard: {total_grains}")
