# 🧩 SudokuApp: A High-Performance Solver & Interactive Game

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Testing](https://img.shields.io/badge/tests-pytest-yellow?style=for-the-badge&logo=pytest)

**SudokuApp** is a robust Python-based application designed for both enthusiasts who love to play Sudoku and developers interested in algorithmic puzzle solving. It features a complete interactive game engine and a powerful backtracking-based solver capable of solving any valid 9x9 Sudoku puzzle.

---

## Key Features

- **Interactive Game Mode**: Play randomly generated Sudoku puzzles with real-time input validation.
- **Automated Backtracking Solver**: A technically sophisticated solver that finds solutions for complex puzzles using recursive backtracking.
- **Dynamic Board Generation**: Generates valid Sudoku boards and removes cells to create unique puzzles.
- **Input Validation**: Robust error handling for user inputs to ensure a seamless experience.
- **Comprehensive Testing**: Includes a full test suite powered by `pytest` for ensuring algorithm reliability.

---

## 🛠️ Technical Architecture

### The Backtracking Algorithm
The core of the solver is a **recursive** backtracking algorithm. It works by:
1. Identifying the next empty cell on the board.
2. Attempting to place digits 1 through 9.
3. Checking if the placement is valid (row, column, and 3x3 subgrid checks).
4. Recursively calling itself to solve the remaining board.
5. Backtracking if a contradiction is found.

This approach ensures that we explore the search space efficiently while finding the correct solution if it exists.

### File Structure
- `project.py`: The entry point of the application containing the game logic and solver.
- `test_project.py`: Contains automated tests for verifying key functions.
- `requirements.txt`: External dependencies required for the project.

---

## 💻 Installation & Usage

### ⚙️ Prerequisites
- Python 3.8 or higher.

### 📥 Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Zer0-Bug/SudokuApp.git
   cd SudokuApp
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 🎮 Running the App
Start the main script to interact with the game menu:
```bash
python project.py
```

---

## 🧪 Testing

We believe in code quality. The project uses `pytest` for unit testing the core logic.

To run the tests:
```bash
pytest test_project.py
```

### Verified Functions:
| Function | Description | Status |
| :--- | :--- | :--- |
| `fill_board` | Board generation logic | ✅ Passed |
| `remove_cells` | Puzzle creation complexity | ✅ Passed |
| `solve_sudoku` | Algorithm correctness | ✅ Passed |

---

## Contribution

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

<p align="center">
  ∞
</p>
