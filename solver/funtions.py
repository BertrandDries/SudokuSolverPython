

def check_box(i, j, sudoku):
    boxrow = (int(i / 3))*3
    boxcollum = (int(j / 3))*3
    for x in range(3):
        for y in range(3):
            if boxrow + x != i and boxcollum + y != j and len(sudoku[boxrow + x][boxcollum + y]) == 1:
                if sudoku[boxrow + x][boxcollum + y][0] in sudoku[i][j]:
                    sudoku[i][j].remove(sudoku[boxrow + x][boxcollum + y][0])


def check_collum(i, j, sudoku):
    for place in range(9):
        if i != place and len(sudoku[place][j]) == 1:
            if sudoku[place][j][0] in sudoku[i][j]:
                sudoku[i][j].remove(sudoku[place][j][0])


def check_row(i, j, sudoku):
    for place in range(9):
        if j != place and len(sudoku[i][place]) == 1:
            if sudoku[i][place][0] in sudoku[i][j]:
                sudoku[i][j].remove(sudoku[i][place][0])


def clean_row(i,sudoku):
    double1=-1
    double2=-1
    for place1 in range(9):
        if len(sudoku[i][place1]) == 2:
            for place2 in range(9):
                 if sudoku[i][place1] == sudoku[i][place2] and place1 != place2 :
                    double1 = place1
                    double2 = place2
    if double1 != -1 and double2 !=-1:
        for number in sudoku[i][double1]:
            for place3 in range(9):
                if len(sudoku[i][place3])>1 and place3 != double1 and place3 != double2 and number in sudoku[i][place3]:
                    sudoku[i][place3].remove(number)

def clean_collum(j,sudoku):
    double1=-1
    double2=-1
    for place1 in range(9):
        if len(sudoku[place1][j]) == 2:
            for place2 in range(9):
                 if sudoku[place1][j] == sudoku[place2][j] and place1 != place2 :
                    double1 = place1
                    double2 = place2
    if double1 != -1 and double2 !=-1:
        for number in sudoku[double1][j]:
            for place3 in range(9):
                if len(sudoku[place3][j])>1 and place3 != double1 and place3 != double2 and number in sudoku[place3][j]:
                    sudoku[place3][j].remove(number)





def fill_empty_spots(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                sudoku[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                sudoku[i][j] = [sudoku[i][j]]


def solve(sudoku):
    fill_empty_spots(sudoku)
    solved = False
    while not solved:
        solved = True
        for i in range(9):
            for j in range(9):
                if len(sudoku[i][j]) > 1:
                    check_row(i, j, sudoku)
                if len(sudoku[i][j]) > 1:
                    check_collum(i, j, sudoku)
                if len(sudoku[i][j]) > 1:
                    check_box(i, j, sudoku)
                if len(sudoku[i][j]) > 1:
                    clean_row(i,sudoku)
                if len(sudoku[i][j]) > 1:
                    clean_collum(j,sudoku)
                if len(sudoku[i][j]) != 1:
                    solved = False

                print("start")
                for line in sudoku:
                    for row in line:
                        print(row)
                print("end")

sudoku = [
    [5, 0, 0, 0, 0, 4, 0, 8, 7],
    [2, 9, 0, 8, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 2, 0, 0],
    [0, 4, 7, 0, 0, 0, 5, 0, 2],
    [0, 8, 5, 9, 0, 7, 1, 4, 0],
    [9, 0, 2, 0, 0, 0, 7, 3, 0],
    [0, 0, 4, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 5, 0, 6, 1],
    [1, 5, 0, 7, 0, 0, 0, 0, 3]
]
sudoku2=[
[0,2,0,0,0,0,1,0,0],
[0,0,0,8,0,0,9,6,0],
[0,6,0,0,0,3,0,5,7],
[0,0,9,0,5,0,0,0,0],
[7,0,0,0,2,0,0,0,9],
[0,0,0,0,7,0,4,0,0],
[5,9,0,6,0,0,0,4,0],
[0,1,2,0,0,5,0,0,0],
[0,0,4,0,0,0,0,9,0]
]
solve(sudoku)
