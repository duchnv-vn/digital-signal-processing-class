import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
f = 5  # Frequency of the sine wave (Hz)
A = 1  # Amplitude of the sine wave
Fs = 1000  # Sampling frequency (Samples per second)
T = 1  # Duration of the signal (Seconds)

# Generate time array and signal
Ts = 1 / Fs
t = np.arange(0, T, Ts)  # Time vector from 0 to T with step size Ts
x = A * np.sin(2 * np.pi * f * t)  # Sine wave signal

# Plot the signal
label = f'{f} Hz Sine Wave'
plt.figure(figsize=(10, 5))
plt.plot(t, x, label=label)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title(label)
plt.grid(True)
plt.legend()
plt.show()
