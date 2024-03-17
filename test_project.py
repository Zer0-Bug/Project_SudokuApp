from project import fill_board, remove_cells, solve_sudoku, is_solution_correct



def test_fill_board():

    board = [[0]*9 for _ in range(9)]
    fill_board(board)
    # Test that some cells are filled
    assert sum(row.count(0) for row in board) < 81





def test_remove_cells():

    board = [[1]*9 for _ in range(9)]
    remove_cells(board, 55)

    # Test that some cells remain
    assert sum(row.count(0) for row in board) < 81





def test_solve_sudoku():
    
    # A solvable sudoku puzzle
    solvable_board = [
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
    assert solve_sudoku(solvable_board) is True
    
    
    # An unsolvable sudoku puzzle
    unsolvable_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]  # A row/column/3x3 box has duplicate numbers
    ]
    assert solve_sudoku(unsolvable_board) is False


