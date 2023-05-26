import Core.Utils as game

board = [
    [0, 0, 4, 6, 7, 2, 0, 0, 0], 
    [5, 0, 0, 8, 0, 0, 0, 9, 6], 
    [0, 6, 3, 0, 4, 0, 0, 0, 8], 
    [3, 8, 2, 1, 0, 0, 9, 6, 0], 
    [4, 7, 5, 0, 0, 0, 1, 0, 0], 
    [9, 1, 0, 2, 0, 4, 5, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 2, 9], 
    [0, 0, 1, 0, 0, 0, 7, 4, 3], 
    [2, 0, 0, 0, 6, 3, 8, 0, 1]
]
new_game = game.Sudoku(board)
new_game.print_board() # prints an empty board
new_game.solve()
print("\n\nSolved sudoku board:\n")
new_game.print_board() # prints a solved board