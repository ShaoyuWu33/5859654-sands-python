import os
import matplotlib.pyplot as plt
from signals import generate_sinusoidal_signal, generate_unit_step, time_shift, time_scale
#1 Generate signals
# Sinusoidal signal parameters
freq = 5           # Hz
duration = 1       # seconds
sampling_rate = 500  # Hz
amplitude = 1
phase = 0          # radians
t, sinusoid = generate_sinusoidal_signal(freq, duration, sampling_rate, amplitude, phase)
# Unit step signal parameter
length = 50
n, step_signal = generate_unit_step(length)

# 2. Apply Transformations
# Time shift
shift_samples = 50
shifted_sinusoid = time_shift(sinusoid, shift_samples)
shifted_step = time_shift(step_signal, 5)

# Time scaling
scale_factor = 0.5  
scaled_sinusoid = time_scale(sinusoid, scale_factor)
scaled_step = time_scale(step_signal, 2)  

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

# Sinusoidal plots
plot_signal(t, sinusoid, "Original Sinusoidal Signal", "Time [s]", "Amplitude", "sinusoid_original.png")
# sinusoidal plots with transformations, "Amplitude")
plot_signal(t, shifted_sinusoid, f"Time-Shifted Sinusoidal (+{shift_samples} samples)", "Time [s]", "sinusoid_shifted.png")

# Unit Step plots
plot_signal(n, step_signal, "Original Unit Step Signal", "n (samples)", "Amplitude", "step_original.png")
# # original unit step plots with transformationsles)", "Amplitude")
plot_signal(n, shifted_step, "Time-Shifted Unit Step Signal", "n (sammples)", "Amplitude", "step_scaled.png")