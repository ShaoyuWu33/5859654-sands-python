import numpy as np
from signals import generate_sinusoidal_signal, generate_unit_step, time_shift, time_scale# 1. Test generate_sinusoidal_signal
def test_generate_sinusoidal_signal():
    """
    Unit test for generate_sinusoidal_signal().
    
    Verifies:
    - Output arrays have equal length.
    - Signal amplitude does not exceed expected range.
    - Signal mean is approximately zero for a full-period sinusoid.
    """
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
    assert abs(np.mean(x)) < 0.1
    
# 2. Test generate_unit_step
def test_generate_unit_step():
    """
    Unit test for generate_unit_step().
    
    Verifies:
    - Output arrays have equal length.
    - Values are only 0 or 1.
    - Signal starts with a step at n = 0.
    """
    n, u = generate_unit_step(10)
    # Check length
    assert len(n) == len(u)
    # Check values (only 0s and 1s)
    assert set(u) == {0, 1}
    # Check step starts at n=0
    assert u[0] == 1

# 3. Test: time_shift
def test_time_shift():
    """
    Unit test for time_shift().
    
    Verifies:
    - Right shift adds zeros to the beginning.
    - Left shift adds zeros to the end.
    - Data shifts correctly.
    """
    x = np.array([1, 2, 3, 4, 5])
    shifted_right = time_shift(x, 2)
    shifted_left = time_shift(x, -2)
    # Right shift → first 2 zeros, rest shifted
    assert np.array_equal(shifted_right[:2], np.zeros(2))
    assert np.array_equal(shifted_right[2:], x[:-2])
    # Left shift → last 2 zeros, rest shifted
    assert np.array_equal(shifted_left[-2:], np.zeros(2))
    assert np.array_equal(shifted_left[:-2], x[2:])

# 4. Test: time_scale
def test_time_scale():
    """
    Unit test for time_scale().
    
    Verifies:
    - Time expansion increases signal length.
    - Time compression decreases signal length.
    """
    x = np.linspace(0, 1, 10)
    scaled_half = time_scale(x, 0.5)   
    scaled_double = time_scale(x, 2)  
    # Expanded signal should have more samples
    assert len(scaled_half) > len(x)
    # Compressed signal should have fewer samples
    assert len(scaled_double) < len(x)

# 5. Run all tests manually
if __name__ == "__main__":
    test_generate_sinusoidal_signal()
    test_generate_unit_step()
    test_time_shift()
    test_time_scale()
    print("All tests passed successfully!")

