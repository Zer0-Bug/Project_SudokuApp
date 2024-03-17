import random
import time

def print_board(board):

    """
    Prints the Sudoku board.

    Args:
        board (list): The Sudoku board represented as a list of lists.

    Returns:
        None
    """

    
    for i in range(len(board)):

        if i % 3 == 0 and i != 0:
            print("- " * 11)

        for j in range(len(board[0])):

            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(board[i][j])

            else:
                print(str(board[i][j]) + " ", end="")



def is_valid(num, board, row, col):

    """
    Checks if placing a number in a given position on the board is valid.

    Args:
        num (int)       : The number to be placed.
        board (list)    : The Sudoku board represented as a list of lists.
        row (int)       : The row index.
        col (int)       : The column index.

    Returns:
        bool            : True if the placement is valid, False otherwise.
    """


    # Check row
    if num in board[row]:
        return False


    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False


    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)

    for i in range(start_row, start_row + 3):

        for j in range(start_col, start_col + 3):

            if board[i][j] == num:
                return False


    return True



def fill_board(board):

    """
    Fills the Sudoku board with valid numbers.

    Args:
        board (list)    : The Sudoku board represented as a list of lists.

    Returns:
        bool            : True if the board is successfully filled, False otherwise.
    """

    
    for row in range(9):
        for col in range(9):

            possible_values = [n for n in range(1, 10) if is_valid(n, board, row, col)]

            if possible_values:
                board[row][col] = random.choice(possible_values)

            else:
                return False
            
    return True



def remove_cells(board, num_cells_to_remove):

    """
    Removes a specified number of cells from the board.

    Args:
        board (list)                : The Sudoku board represented as a list of lists.
        num_cells_to_remove (int)   : The number of cells to be removed.

    Returns:
        None
    """


    cells = [(row, col) for row in range(9) for col in range(9)]

    random.shuffle(cells)

    for i in range(81 - num_cells_to_remove):
        row, col = cells[i]
        board[row][col] = 0


def is_board_full(board):

    """
    Checks if the Sudoku board is full.

    Args:
        board (list)  : The Sudoku board represented as a list of lists.

    Returns:
        bool          : True if the board is full, False otherwise.
    """

    
    for row in board:
        if 0 in row:
            return False
        
    return True



def is_solution_correct(board):

    """
    Checks if the Sudoku solution is correct.

    Args:
        board (list)    : The Sudoku board represented as a list of lists.

    Returns:
        bool            : True if the solution is correct, False otherwise.
    """


    def is_valid(num, row, col):

        # Check row
        if num in board[row]:
            return False


        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False


        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True



    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:
                return False
            
            num = board[row][col]

            board[row][col] = 0

            if not is_valid(num, row, col):
                board[row][col] = num
                return False
            
            board[row][col] = num


    return True



def solve_sudoku(board):

    """
    Solves the Sudoku board using backtracking algorithm.

    Args:
        board (list)    : The Sudoku board represented as a list of lists.

    Returns:
        bool            : True if the board is solvable, False otherwise.
    """


    def find_empty_cell(board):

        for i in range(9):
            for j in range(9):

                if board[i][j] == 0:
                    return (i, j)
                
        return None



    def is_valid_in_row(board, row, num):

        for col in range(9):
            if col != find_column_with_number(board, row, num) and board[row][col] == num:
                return True
        return False



    def is_valid_in_column(board, col, num):

        for row in range(9):
            if row != find_row_with_number(board, col, num) and board[row][col] == num:
                return True
        return False



    def find_column_with_number(board, row, num):

        for col in range(9):
            if board[row][col] == num:
                return col
        return -1



    def find_row_with_number(board, col, num):

        for row in range(9):
            if board[row][col] == num:
                return row
        return -1



    def check_cell_consistency(board):

        for row in range(9):
            for col in range(9):
                if board[row][col] != 0:
                    if is_valid_in_row(board, row, board[row][col]) or is_valid_in_column(board, col, board[row][col]):
                        return False
        return True



    def solve(board):

        if not check_cell_consistency(board):
            return False

        empty_cell = find_empty_cell(board)

        if not empty_cell:
            return True
        
        else:
            row, col = empty_cell


        for num in range(1, 10):

            if is_valid(num, board, row, col):
                board[row][col] = num

                if solve(board):
                    return True

                board[row][col] = 0

        return False

    return solve(board)



def get_user_input():

    """
    Gets the user input for entering a Sudoku board.

    Returns:
        list    : The user-entered Sudoku board represented as a list of lists.
    """


    print("Enter the Sudoku board (9x9) row by row:\n")

    board = []


    for i in range(9):

        while True:

            row_input = input(f"Enter row {i+1} (9 numbers separated by spaces): ").strip()

            if len(row_input) == 0:
                print("\nPlease enter a row.")
                continue

            row = row_input.split()

            if len(row) != 9:
                print("\nInvalid input! Please enter exactly 9 numbers.\n")
                continue

            row = [int(num) for num in row]

            if any(num < 0 or num > 9 for num in row):
                print("\nInvalid input! Please enter numbers between 0 and 9.")
                continue

            board.append(row)
            break


    return board



def start():

    """
    Starts the Sudoku game or solver based on user's choice.
    """


    print("==================================================")
    choice = input("\n '1' to Play Sudoku\n" + " '2' to Solve Sudoku\n" + " 'Exit' to Exit \n")
    print("==================================================")


    if choice == '1' or choice == '2':



        if choice == '1':

            board = [[0]*9 for _ in range(9)]

            fill_board(board)

            remove_cells(board, 55)
            

            print("\nWelcome to Sudoku Game!")
            time.sleep(1)
            print("Let's play Sudoku.")
            time.sleep(1)
            print("To place a number, enter row number, column number, and the number to place.")
            time.sleep(2)
            print("Go!")
            time.sleep(1)
            print("==================================================\n")


            while not is_board_full(board):
                print_board(board)


                try:
                    row = int(input("\nEnter row number (1-9): ")) - 1
                    col = int(input("Enter column number (1-9): ")) - 1
                    num = int(input("Enter the number to place (1-9): \n"))
                    print("==================================================\n")

                except ValueError:
                    print("==================================================")
                    print("\nInvalid input! Please enter a number.\n")
                    continue


                if row < 0 or row > 8 or col < 0 or col > 8 or num < 1 or num > 9:
                    print("\nInvalid input! Please enter row, column, and number within the range of 1-9.")
                    continue


                if board[row][col] != 0:
                    print("==================================================")
                    print("\nThat cell is already filled. Choose another one.\n")
                    continue


                if not is_valid(num, board, row, col):
                    print("==================================================")
                    print("\nInvalid placement! Try again.\n")
                    continue


                board[row][col] = num

            print_board(board)


            if is_solution_correct(board):
                print("==================================================")
                print("\nCongratulations! You solved the Sudoku correctly!\n")

            else:
                print("==================================================")
                print("\nSorry, the solution is incorrect. Better luck next time!\n")





        elif choice == '2':

            user_board = get_user_input()

            print("\n====================")
            print("\nEntered Sudoku board:")


            for i, row in enumerate(user_board):

                if i % 3 == 0:
                    print("- " * 11)

                print(" ".join(map(str, row[:3])) + " | " + " ".join(map(str, row[3:6])) + " | " + " ".join(map(str, row[6:])))


            if i == 8:
                print("- " * 11)


            if solve_sudoku(user_board):
                print("====================")
                print("\nSudoku Solution:")
                print_board(user_board)
                print("\n====================\n")

            else:
                print("==================================================")
                print("\n> >  This Sudoku puzzle does not have a solution.\n")
                print("==================================================")


    elif choice.lower() == 'exit':
        print("Exiting...")
        exit()


    else:
        print("Invalid input. Please try again.")
        start()


def main():

    """
    Main function to start the Sudoku game.
    """


    print("\n        W e l c o m e ")
    time.sleep(1)
    print("            t o ")
    time.sleep(1)
    print("  S u d o k u   A  p  p ! ")
    time.sleep(3)

    print("\nPlay a Sudoku game if you want, or enter the Sudoku you can't solve and see the result!")
    time.sleep(5)

    start()

if __name__ == "__main__":
    main()