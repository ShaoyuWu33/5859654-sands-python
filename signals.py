# Contains functions for signal generation and signal operations. 
Includes at least two signal generators and two signal transformations
import numpy as np
def generate_sinusoidal_signal(frequency, duration, sampling_rate, amplitude, phase):
    """
    Generate a continuous sinusoidal (sine) signal.

    Parameters
    ----------
    frequency : float
        Frequency of the sinusoid in hertz (Hz).
    duration : float
        Duration of the signal in seconds.
    sampling_rate : float
        Sampling rate in samples per second (Hz).
    amplitude : float
        Peak amplitude of the sinusoid.
    phase : float
        Initial phase offset in radians.

    Returns
    -------
    t : numpy.ndarray
        Array of time values corresponding to each sample.
    x : numpy.ndarray
        Generated sinusoidal signal values.

    Notes
    -----
    The function uses the formula:
        x(t) = A * sin(2πft + φ)
    where A = amplitude, f = frequency, φ = phase.
    """
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    x = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return t, x

def
    """
    Generate a discrete-time unit step signal.

    Parameters
    ----------
    length : int
        Number of samples in the signal.

    Returns
    -------
    n : numpy.ndarray
        Sample indices (0 to length-1).
    u : numpy.ndarray
        Unit step values (1 for n >= 0, 0 otherwise).

    Notes
    -----
    This is a discrete step function where:
        u[n] = 1 for n >= 0
        u[n] = 0 for n < 0
    """ generate_unit_step(length):
    n = np.arange(length)
    u = np.where(n >= 0, 1, 0)
    return n, u

def time_shi
    """
    Perform a time shift (delay or advance) on a discrete signal.

    Parameters
    ----------
    signal : numpy.ndarray
        Input signal array.
    shift : int
        Number of samples to shift.
        Positive → right shift (delay)
        Negative → left shift (advance)

    Returns
    -------
    shifted_signal : numpy.ndarray
        Time-shifted version of the input signal.

    Notes
    -----
    The signal adds zeros on the side opposite to the shift direction.
    """ft(signal: np.array, shift):
    if shift > 0:
        shifted_signal = np.concatenate((np.zeros(shift), signal[:-shift]))
    elif shift < 0:
        shifted_signal = np.concatenate((signal[-shift:], np.zeros(-shift)))
    else:
        shifted_signal = signal
    return shifted_signal

def time_scale(signal: np.array, scale):
    n = np.arange(len(signal))
    new_length = int(len(signal) / scale)
    new_n = np.linspace(0, len(signal) - 1, new_length)
    scaled_signal = np.interp(new_n, n, signal)
    return scaled_signal