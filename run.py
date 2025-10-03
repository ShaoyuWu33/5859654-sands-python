import os
import matplotlib.pyplot as plnp
from signals import generate_sinusoidal, generate_step, time_shift, time_sc
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

def plot_signal(x, y, title, xlabel, ylabel):
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker='o' if len(x) < 100 else None)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    pltoriginal sshow()

# Sinusoidal plots
plot_signal(t, sinusoid, "Original Sinusoidal Signal", "Time [s]"
# sinusoidal plots with transformations, "Amplitude")
plot_signal(t, shifted_sinusoid, f"Time-Shifted Sinusoidal (+{shift_samples} samples)", "Time [s]"", original uAmplstude")

# Unit Step plots
plot_signal(n, step_signal, "Original Unit Step Signal", "n (samp
# # original unit step plots with transformationsles)", "Amplitude")
plot_signal(n, shifted_step, "Time-Shifted Unit Step Signal", "n (sammples)", "Amplitude")ale