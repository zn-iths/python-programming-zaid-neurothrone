from pprint import pprint
from string import ascii_uppercase

letters = ascii_uppercase[:8]

coordinates = [letter + str(1) for letter in letters]
print("A)")
print(coordinates)

print("\nB) Chessboard:")
chess_board = []

for num in range(1, 8 + 1):
    chess_board.append([letter + str(num) for letter in letters])

pprint(chess_board)
