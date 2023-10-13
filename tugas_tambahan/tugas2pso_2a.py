import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1  # Amplitude
f_s = 1000  # Sampling frequency
T = 1 / f_s  # Sampling period

# Time domain
t = np.linspace(-1, 1, 2 * f_s, endpoint=False)  # Time range from -1 to 1 seconds
frequencies = np.fft.fftfreq(len(t), T)  # Frequencies for FFT

# Fourier Sinc Function 1: F(f) = 2A sinc (2fA)
sinc_function_1 = 2 * A * np.sinc(2 * A * t)

# Fourier Sinc Function 2: F(f) = A sinc (fA)
sinc_function_2 = A * np.sinc(A * t)

# Fourier Sinc Function 3: F(f) = 6A sinc (6fA)
sinc_function_3 = 6 * A * np.sinc(6 * A * t)

# FFT
fft_sinc_function_1 = np.fft.fft(sinc_function_1)
fft_sinc_function_2 = np.fft.fft(sinc_function_2)
fft_sinc_function_3 = np.fft.fft(sinc_function_3)

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(3, 2, 1)
plt.plot(t, sinc_function_1)
plt.title('F(f) = 2A sinc (2fA)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 2)
plt.plot(frequencies, np.abs(fft_sinc_function_1))
plt.title('1D FFT of F(f) = 2A sinc (2fA)')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 3)
plt.plot(t, sinc_function_2)
plt.title('F(f) = A sinc (fA)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 4)
plt.plot(frequencies, np.abs(fft_sinc_function_2))
plt.title('1D FFT of F(f) = A sinc (fA)')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 5)
plt.plot(t, sinc_function_3)
plt.title('F(f) = 6A sinc (6fA)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 6)
plt.plot(frequencies, np.abs(fft_sinc_function_3))
plt.title('1D FFT of F(f) = 6A sinc (6fA)')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
