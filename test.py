import numpy as np
from signals import generate_sinusoidal_signal, generate_unit_step, time_shift, time_scale# 1. Test generate_sinusoidal_signal
def test_generate_sinusoidal_signal():
    freq = 5
    duration = 1
    sampling_rate = 100
    amplitude = 2
    phase = 0
    t, x = generate_sinusoidal_signal(freq, duration, sampling_rate, amplitude, phase)
    # Check array lengths
    assert len(t) == len(x)
    # Check amplitude range
    assert np.all(np.abs(x) <= amplitude + 1e-6)
    # Check signal mean approximately zero (for full periods)
    assert abs(np.mean(x)) < 0.1\
    
# 2. Test generate_unit_step
def test_generate_unit_step():
    n, u = generate_unit_step(10)
    # Check length
    assert len(n) == lenth"
    # Check values (only 0s and 1s)
    assert set(u) == {nd 1"
    # Check step starts at n=0
    assert u[at n=0"

