from signals import generate_sine_wave
import matplotlib.pyplot as plt

sine_wave = generate_sine_wave(frequency=5, duration=2, sample_rate=100)
# Create time points for plotting
t = np.linspace(0, 2, int(2 * 100))

plt.plot(t, sine_wave)
plt.title('Sine Wave (5 Hz)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')