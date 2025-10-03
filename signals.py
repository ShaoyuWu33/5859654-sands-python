# Contains functions for signal generation and signal operations. 
Includes at least two signal generators and two signal transformations
import numpy as np
def generate_sinusoidal_signal(frequency, duration, sampling_rate, amplitude, phase):
    t = np.linspace(0, duration, int(sampling_rate * duration, endpoint=False))
    x = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return t, x

def generate_unit_step(length):
    n = np.arange(length)
    u = np.where(n >= 0, 1, 0)
    return n, u.