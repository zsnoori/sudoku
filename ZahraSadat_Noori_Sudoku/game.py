import Core.Utils as game
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("board")
args = parser.parse_args()
board_str = args.board
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

board_str = board_str.replace(',', '').replace('[','').replace(']','')
for i in range(9):
  for j in range(9):
    board[i][j]=int(board_str[i*9+j])


new_game = game.Sudoku(board)
#  print input(unsolved) sudoku
new_game.print_board() 
new_game.solve()
print("\n\nSolved sudoku board:\n")
new_game.print_board()