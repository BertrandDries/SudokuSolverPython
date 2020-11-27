sudokufile = open(r"C:/Users/Dries/Desktop/sudoku.txt", "r")
sudoku = [[], [], [], [], [], [], [], [], []]
i = 0
for line in sudokufile:
    sudoku[i] = line
    i += 1
sudokufile.close()

solve(sudoku)
