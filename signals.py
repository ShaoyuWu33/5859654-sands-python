import numpy as np

def generate_sine_wave(frequency, duration, sample_ratents
    t = np.linspace(0, duration, int(duration * sample_ra wave
    sine_wave = np.sin(2 * np.pi * frequency * t)
    return sine_wave