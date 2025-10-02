# signals and systems Python project
# 1. Project Description
This README file contains a Python-based signal processing project designed to demonstrate signal generation, such as time-shifting, time-scaling, etc, signal transformations, and visualization using Python. The project adheres to modular software design principles, utilizes version control (Git), and includes comprehensive documentation to ensure reproducibility and readability. It aligns with the requirements for the "Signals and Systems" (S&S) course, with support for mid-term (core functionality) and final (testing, packaging) submissions.
# 2. Project Structure
The project is organized into different files to separate tasks (signal generation, execution, testing, and configuration).- signals.py          # Core: Signal generation + signal operation functions (with docstrings)-─ run.py              # Execution: Imports/calls functions, plots signals, saves output-── test_signals.py     # Testing: Unit tests for functions in signals.py (required for fina-├── pyproject.toml      # Packaging: Metadata, dependencies (e.g., numpy, matplotlib, pyte-
├── generated_plots/    # Auto-created folder: Stores saved signal plots (run.py generates t-
└── README.md           # Documentation: Project setup, usage, theory, and d
# 3.Basic Background Theory
This project implements fundamental concepts from Signals and Systems
1. Generate signals
-Sinusoidal signals: x(t)=A⋅sin(2πft+ϕ)
A = amplitude, f = frequency (Hz), ϕ = phase (radians
-Unit Step Signal: u(t)=1
for t>=0, u(t)=0 for t<0
2. Signal Transformations
-Time Shifting: x(t-t0)
t0>0: shift right
t0<0: shift left
-Time Scaling:etails