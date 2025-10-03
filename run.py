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
n, step_signal = generate_unit_step(length)ale