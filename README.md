# signals and systems Python project
# 1. Project Description
This README file contains a Python-based signal processing project designed to demonstrate signal generation, such as time-shifting, time-scaling, etc, signal transformations, and visualization using Python. The project adheres to modular software design principles, utilizes version control (Git), and includes comprehensive documentation to ensure reproducibility and readability. It aligns with the requirements for the "Signals and Systems" (S&S) course, with support for mid-term (core functionality) and final (testing, packaging) submissions.
# 2. Project Structure
The project is organized into different files to separate tasks (signal generation, execution, testing, and configuration).1.─ signals.py          # Core: Signal generation + signal operation functions (with docstrings)2.── run.py              # Execution: Imports/calls functions, plots signals, saves output3.├── test_signals.py     # Testing: Unit tests for functions in signals.py (required for fina4.
├── pyproject.toml      # Packaging: Metadata, dependencies (e.g., numpy, matplotlib, pyte5.
├── generated_plots/    # Auto-created folder: Stores saved signal plots (run.py generates t6.)
└── README.md           # Documentation: Project setup, usage, theory, and details