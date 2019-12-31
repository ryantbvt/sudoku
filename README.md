# sudoku
Code inspired by TechWithTim from Youtube

His code is linked here: https://github.com/techwithtim/Sudoku-GUI-Solver

I followed his tutorial on how to code sudoku
and understood the core element of this program, 
which was the backtracking algorithm

The backtracking algorithm is an algorithm using recursion
to continously check if the answers on the sudoku board is
correct based on what is already there, and what's being inserted.

If there are no values that can be inserted, the code goes back
and inserts a new set of numbers so that it can continue to solve the board.

If it cannot, the sudoku board isn't solvable

# instructions (from techwithtim's description)

Click a box and hit the number on your keybaord to pencil in a number. To confirm that value press the ENTER key on that box. To delete a pencil in you can click DEL. Finally to solve the board press SPACE, sit back and watch the algorithm run.
