import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
T = 1
Fs = 25

# Generate time array and signal
Ts = 1 / Fs
t = np.arange(0, T, Ts)
y = np.sin(2 * np.pi * 8 * t)

# Plot the signal
label = f'{Fs} Hz Sine Wave'
plt.plot(t, y, label=label)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title(label)
plt.grid(True)
plt.legend()
plt.show()
