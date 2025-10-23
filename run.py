import numpy as np
import matplotlib.pyplot as plt
from signals import generate_sinusoidal_signal, generate_unit_step, time_shift, time_scale
#1 Generate signals
# Sinusoidal signal parameters
freq = 5           # Hz
duration = 1       # seconds
sampling_rate = 500  # Hz
amplitude = 1
phase = 0          # radians
# Generate continuous-looking sinusoid
t, sinusoid = generate_sinusoidal_signal(freq, duration, sampling_rate, amplitude, phase)
# Unit step signal parameter
length = 100
n, step_signal = generate_unit_step(length)

# 2. Apply Transformations
# Time shift
shift_samples = 50
shifted_sinusoid = time_shift(sinusoid, shift_samples)
shifted_step = time_shift(step_signal, 5)

# Time scaling
scale_factor = 0.5  
scaled_sinusoid = time_scale(sinusoid, scale_factor)
scaled_step = time_scale(step_signal, scale_factor)  

# --- Apply amplitude scaling rule for unit step ---
# u(t) = 1/scale for t >= 0
scaled_step *= (1 / scale_factor)

# Recalculate time vectors for scaled signals
t_scaled = np.linspace(0, duration / scale_factor, len(scaled_sinusoid)) 
n_scaled = np.linspace(n[0], n[-1] / scale_factor, len(scaled_step))     

# 3. Plot Signals

def plot_signal(x, y, title, xlabel, ylabel, plot_name):
    """
    Plot a signal and save it as an image file.

    Parameters
    ----------
    x : numpy.ndarray
        Independent variable (time or sample index).
    y : numpy.ndarray
        Dependent variable (signal amplitude).
    title : str
        Plot title.
    xlabel : str
        Label for the x-axis.
    ylabel : str
        Label for the y-axis.
    plot_name : str
        File name for saving the figure (e.g., 'signal.png').

    Returns
    -------
    None
        The function displays and saves the plot.

    Notes
    -----
    If the signal length is short (<100 points), markers are added for clarity.
    """
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker='o' if len(x) < 100 else None)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.savefig(plot_name)

# sinusoidal plots
plot_signal(t, sinusoid, "Original Sinusoidal Signal", "Time [s]", "Amplitude", "sinusoid_original.png")
# sinusoidal plots with a time shift
plot_signal(t, shifted_sinusoid, f"Time-Shifted Sinusoidal (+{shift_samples} samples)", "Time [s]","Amplitude", "sinusoid_shifted.png")
# sinusoidal plots with time scaling
plot_signal(t_scaled, scaled_sinusoid, f"Time-Scaled Sinusoidal (scale={scale_factor})", "Time [s]", "Amplitude", "sinusoid_scaled.png")

# unit Step plots
plot_signal(n, step_signal, "Original Unit Step Signal", "t", "u(t)", "step_original.png")
# unit step plots with a time shift
plot_signal(n, shifted_step, "Time-Shifted Unit Step Signal", "t", "u(t)", "step_shifted.png")
# unit step plots with time scaling
plot_signal(n_scaled, scaled_step, f"Time-Scaled Unit Step Signal (scale={scale_factor})", "t", "u(t)", "step_scaled.png")