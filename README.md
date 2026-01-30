<h1 align="center">SudokuApp</h1>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://docs.pytest.org/">
    <img src="https://img.shields.io/badge/Testing-Pytest-yellowgreen?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-darkred?style=for-the-badge" alt="License">
  </a>
</p>

<p align="center">
  <b>A high-performance Sudoku engine featuring an interactive game and an automated solver.</b><br><br>
  <i>Leveraging recursive backtracking for efficient puzzle solving and a robust terminal-based interface for gameplay.</i>
</p>
<br>
<p align="center">
  <a href="#technical-architecture">
    <img src="https://img.shields.io/badge/Architecture-222222?style=flat" />
  </a>
  <span> ° </span>
  <a href="#project-structure">
    <img src="https://img.shields.io/badge/Structure-222222?style=flat" />
  </a>
  <span> ° </span>
  <a href="#key-features">
    <img src="https://img.shields.io/badge/Features-222222?style=flat" />
  </a>
  <span> ° </span>
  <a href="#technical-specifications">
    <img src="https://img.shields.io/badge/Specs-222222?style=flat" />
  </a>
  <span> ° </span>
  <a href="#deployment--installation">
    <img src="https://img.shields.io/badge/Deploy-222222?style=flat" />
  </a>
</p>

---
<br>
<h2 align="center">Technical Architecture</h2>

The application is architected to balance algorithmic efficiency with user interactivity. At its core, it implements a **Constraint Satisfaction** approach to Sudoku solving:

1.  **Backtracking Solver:** A recursive algorithm that explores the search space by placing digits and pruning branches as soon as a constraint (Row, Column, or 3x3 Box) is violated.
2.  **Board Generation:** Utilizes a randomized filling strategy followed by a cell-removal process to generate unique puzzles with varying difficulty.
3.  **State Management:** The board is maintained as a 2D matrix (list of lists) with real-time validation checks during both manual play and automated solving.
4.  **Terminal Interface:** Uses Python's standard I/O for a lightweight, dependency-free command-line experience.

---
<br>
<h2 align="center">Project Structure</h2>

```
SudokuApp/
├── project.py                                # Main orchestrator and core logic
├── test_project.py                          # Automated test suite using pytest
├── requirements.txt                          # Python dependencies manifest
├── LICENSE                                   # MIT License terms
├── README.md                                 # Project documentation
│
└── .git/                                     # Version control repository
```

---
<br>
<h2 align="center">Key Features</h2>

### 1. Interactive Game Mode
Experience Sudoku directly in your terminal. The game mode provides:
- **Puzzle Generation:** Dynamic creation of 9x9 Sudoku boards.
- **Real-Time Validation:** Immediate feedback on invalid placements.
- **Completion Check:** Automated verification of the final solution.

### 2. Automated Backtracking Solver
Solve any valid 9x9 Sudoku puzzle instantly.
- **Heuristic Exploration:** Efficiently finds solutions using recursive depth-first search.
- **Consistency Checking:** Ensures the input board is valid before attempting a solution.

---
<br>
<h2 align="center">Technical Specifications</h2>

<table align="center">
  <tr>
    <th align="center">Aspect</th>
    <th align="center">Details</th>
  </tr>
  <tr>
    <td align="center">Language</td>
    <td align="center">Python 3.8+</td>
  </tr>
  <tr>
    <td align="center">Solving Algorithm</td>
    <td align="center">Recursive Backtracking (DFS)</td>
  </tr>
  <tr>
    <td align="center">Testing Framework</td>
    <td align="center">Pytest</td>
  </tr>
  <tr>
    <td align="center">Board Generation</td>
    <td align="center">Randomized Filling + Cell Removal</td>
  </tr>
</table>

---
<br>
<h2 align="center">Deployment & Installation</h2>

### 1. Repository Acquisition
Obtain a local copy of the repository:
```bash
git clone https://github.com/Zer0-Bug/SudokuApp.git
```

### 2. Environment Setup
Install the necessary dependencies to run tests and the application:
```bash
cd SudokuApp
```
```bash
pip install -r requirements.txt
```

### 3. Running the Application
Launch the interactive menu to start playing or solving:
```bash
python project.py
```

### 4. Running Tests
Execute the test suite to verify algorithm integrity:
```bash
pytest test_project.py
```

---
<br>
<h2 align="center">Contribution</h2>

Contributions are welcome! If you have suggestions for performance improvements or new features, feel free to contribute:

1. Fork the repository.
2. Create a new branch for your change:  
   `git checkout -b feature/your-feature-name`
3. Commit your changes with a clear and descriptive message:  
   `git commit -m "Add: brief description of the change"`
4. Push your branch to your fork:  
   `git push origin feature/your-feature-name`
5. Open a Pull Request describing the changes made.

All contributions are reviewed before being merged. Please ensure that your changes follow the existing code style and include relevant documentation or tests where applicable.

---

<br>
<p align="center">
  <a href="mailto:777eerol.exe@gmail.com">
    <img src="https://cdn.simpleicons.org/gmail/D14836" width="40" alt="Email">
  </a>
  <span> × </span>
  <a href="https://www.linkedin.com/in/eerolexe/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
         width="40"
         alt="LinkedIn">
  </a>
</p>

---
