# Sudoku Solver and Game

This Python program allows users to play Sudoku or solve Sudoku puzzles programmatically. Sudoku is a popular puzzle game that requires filling a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids contain all of the digits from 1 to 9.

## Features

- **Sudoku Game**: Users can play Sudoku with randomly generated puzzles.
- **Sudoku Solver**: Users can input their own Sudoku puzzle and get the solution if it exists.
- **User Interaction**: User-friendly interface with instructions and error handling for inputs.
- **Backtracking Algorithm**: Sudoku solver utilizes a backtracking algorithm to find the solution efficiently.
- **Board Generation**: Random Sudoku board generation with a specified number of empty cells.

## Usage

To start the program, simply run the `main()` function in the `project.py` file.

python project.py

---

The program will prompt you to choose whether you want to play Sudoku or solve a Sudoku puzzle. Follow the on-screen instructions for further interactions.

## Requirements

- Python 3.x

## How It Works

The program utilizes a combination of board generation, backtracking algorithm, and user input handling to provide a seamless experience for playing Sudoku or solving Sudoku puzzles.

### Board Generation

The Sudoku board is randomly generated with a certain number of cells filled. The number of filled cells can be adjusted for varying difficulty levels.

### Backtracking Algorithm

The Sudoku solver uses a backtracking algorithm to recursively fill in empty cells while ensuring that the Sudoku rules are not violated.

### User Interaction

The program guides the user through the Sudoku game or puzzle-solving process with clear instructions and error messages for invalid inputs.

---

## Testing

The project includes a test suite to ensure the correctness of its functionalities. The test cases are defined in the `test_project.py` file and can be run using any Python testing framework such as `unittest` or `pytest`.

### Test Cases

#### `test_fill_board()`

- **Description**: Tests the `fill_board()` function to ensure that it fills the Sudoku board with some numbers.
- **Approach**: Generates an empty Sudoku board and fills it using the `fill_board()` function. Then, checks if there are fewer empty cells than the total number of cells.
- **Expected Outcome**: The test passes if there are fewer empty cells than the total number of cells after filling the board.

#### `test_remove_cells()`

- **Description**: Tests the `remove_cells()` function to ensure that it removes a specified number of cells from the Sudoku board.
- **Approach**: Generates a Sudoku board with all cells filled, then removes cells using the `remove_cells()` function. Checks if there are still some filled cells left on the board.
- **Expected Outcome**: The test passes if there are still some filled cells left on the board after removing cells.

#### `test_solve_sudoku()`

- **Description**: Tests the `solve_sudoku()` function to ensure that it correctly solves solvable Sudoku puzzles and returns False for unsolvable ones.
- **Approach**: Provides both solvable and unsolvable Sudoku boards as input to the function. Checks if the function returns True for solvable boards and False for unsolvable boards.
- **Expected Outcome**: The test passes if the function returns True for solvable Sudoku boards and False for unsolvable ones.


### Running Tests

To run the test suite for the project, follow these steps:

1. Ensure that you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

2. Navigate to the root directory of the project using the command line or terminal.

3. Install the necessary dependencies. If you haven't already installed `pytest`, you can do so using pip:

`pip install pytest`


4. Once the dependencies are installed, run the test suite by executing the following command:

`pytest test_project.py`


5. After running the tests, pytest will display the results along with any failures or errors encountered during the test execution.

6. If all tests pass successfully, you'll see a summary indicating the number of tests run and their status.

---

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests for any improvements or additional features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.