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
    return n, u

def time_shift(signal: np.array, shift):
    if shift > 0:
        shifted_signal = np.concatenate((np.zeros(shift), signal[:-shift]))
    elif shift < 0:
        shifted_signal = np.concatenate((signal[-shift:], np.zeros(-shift)))
    else:
        shifted_signal = signal
    return shifted_signal.