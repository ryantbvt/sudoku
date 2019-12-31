'''
this class solves the sudoku board
'''

# board = [
#         [7, 8, 0, 4, 0, 0, 1, 2, 0],
#         [6, 0, 0, 0, 7, 5, 0, 0, 9],
#         [0, 0, 0, 6, 0, 1, 0, 7, 8],
#         [0, 0, 7, 0, 4, 0, 2, 6, 0],
#         [0, 0, 1, 0, 5, 0, 9, 3, 0],
#         [9, 0, 4, 0, 6, 0, 0, 0, 5],
#         [0, 7, 0, 3, 0, 0, 0, 1, 2],
#         [1, 2, 0, 0, 0, 7, 4, 0, 0],
#         [0, 4, 9, 2, 0, 6, 0, 0, 7]
# ]

board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

''' 
solve sudoku board
@param boa the array of the board
@return true if the board is solved
'''
def solve(boa):
    # base case
    find = find_empty(boa)

    if find:
        row, col = find
    
    else:
        return True
    # end base case

    for i in range(1,10):
        if valid(boa, i, (row, col)):
            boa[row][col] = i

            if solve(boa):
                return True
            
            boa[row][col] = 0

    return False

# prints the board out to the terminal
# @param boa the array of the board
def print_board(boa):
    for i in range(len(boa)):
        if i % 3 == 0 and i != 0: # separates each row of boxes
            print("- - - - - - - - - - - -")

        for j in range(len(boa[0])):
            if j % 3 == 0 and j != 0: # separates each column
                print(" | ", end = "")

            if j == 8:
                print(boa[i][j], end = "\n")

            else:
                print(str(boa[i][j]) + " ", end = "")

# find the empty positions of the board
# @param boa the array of the board
# @return the empty positions
def find_empty(boa):
    for i in range(len(boa)):
        for j in range(len(boa[0])):
            if boa[i][j] == 0:
                return (i, j) # row, col
    
    return None

'''
checks the number inserted is valid
@param boa the array of the board
@param num the number being inserted and tested
@param pos the position of the empty position in the board
@return if the number being entered is good or not (true or false)
'''
def valid(boa, num, pos):
    # check row
    for i in range(0,len(boa)):
        if boa[pos[0]][i] == num and pos[1] != i:
            return False

    # check the column
    for i in range(0,len(boa)):
        if boa[i][pos[1]] == num and pos[0] != i:
            return False
    
    # check the square that the number is in
    square_x = pos[1] // 3
    square_y = pos[0] // 3

    # loop through all the squares
    for i in range(square_y*3, square_y*3 + 3):
        for j in range(square_x*3, square_x*3 + 3):
            if boa[i][j] == num and (i,j) != pos:
                return False

    return True

print_board(board)
print("______________________")
solve(board)
print_board(board)