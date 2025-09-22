from signals import generate_sine_wave
sine_wave = generate_sine_wave(frequency=5, duration=2, sample_rate=100)
print("First 10 samples of the sine wave:")
print(sine_wave[:10])