# signals and systems Python project
# 1. Project Description
This README file contains a Python-based signal processing project designed to demonstrate signal generation, such as time-shifting, time-scaling, etc, signal transformations, and visualization using Python. The project adheres to modular software design principles, utilizes version control (Git), and includes comprehensive documentation to ensure reproducibility and readability. It aligns with the requirements for the "Signals and Systems" (S&S) course, with support for mid-term (core functionality) and final (testing, packaging) submissions.
# 2. Project Structure
The project is organized into different files to separate tasks (signal generation, execution, testing, and configuration).1. ** signals.p**
   -  Core: Signal generation + signal operation functions (with docstrings)2 **─ run.**
   - # Execution: Imports/calls functions, plots signals, saves output3. **── test_signals**
   -  # Testing: Unit tests for functions in signals.py (required for fina5. **├── pyproject.**
   -   # Packaging: Metadata, dependencies (e.g., numpy, matplotlib, pyte7. **
├── generated_**
   -    # Auto-created folder: Stores saved signal plots (run.py generates t9. **
└── REA**
    -     # Documentation: Project setup, usage, theory, and d
# 3.Basic Background Theory
This project implements fundamental concepts from Signals and Systems
1. **Generate signals**
-'Sinusoidal signals: x(t)=A⋅sin(2πft+ϕ)'
A = amplitude, f = frequency (Hz), ϕ = phase (radians)
-Unit Step Signal: u(t)=1
for t>=0, u(t)=0 for t<0
2. **Signal Transformations**
-`Time Shifting: x(t-t0)` 
→t0>0: shift right
→t0<0: shift left
-`Time Scaling: x(at)`
→a > 1: Signal is compressed
→0 < a < 1: Signal is expanded
# 4. Method Implemented
1. **Function Definitions (in `signals.py`)**  
   - `generate_sinusoidal(frequency, duration, sampling_rate)`  
     → Creates a sinusoidal signal with adjustable frequency, duration, and sampling rate.  
   - `generate_step(length)`  
     → Generates a discrete-time unit step signal of a given length.  
   - `time_shift(signal, shift)`  
     → Shifts a signal by a specified number of samples (positive = delay, negative = advance).  
   - `time_scale(signal, scale)`  
     → Scales the signal along the time axis, compressing or stretching it.  

2. **Execution (in `script.py`)**  
   - Imports the functions from `signals.py`.  
   - Calls signal generators and operations with specified arguments.  
   - Uses `matplotlib` to plot the original and transform in reports.  

3. **Testing (in `tests.py`, final submission only)**  
   - Includes unit tests to validate correctness of implemented functions.  
   - Tests can be run with `pytest`.  

4. **Documentation and Packaging**  
   - Each function includes **docstrings** describing parameters and outputs.  
   - `README.md` documents the project concept, methods, and usage.  
   - `pyproject.toml` provides metadata and dependencies for packaging.etails