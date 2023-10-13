# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:02:41 2023

@author: ACER
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1  # Amplitude
f_s = 100  # Sampling frequency
T = 1 / f_s  # Sampling period

# Create a grid in spatial domain
x = np.linspace(-1, 1, 2 * f_s, endpoint=False)  # x-axis values
y = np.linspace(-1, 1, 2 * f_s, endpoint=False)  # y-axis values
xx, yy = np.meshgrid(x, y)  # 2D grid

# Fourier Sinc Function 1: F(f) = 2A sinc (2fA)
sinc_function_1 = 2 * A * np.sinc(2 * A * xx) * np.sinc(2 * A * yy)

# Fourier Sinc Function 2: F(f) = A sinc (fA)
sinc_function_2 = A * np.sinc(A * xx) * np.sinc(A * yy)

# Fourier Sinc Function 3: F(f) = 6A sinc (6fA)
sinc_function_3 = 6 * A * np.sinc(6 * A * xx) * np.sinc(6 * A * yy)

# 2D FFT
fft_sinc_function_1 = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(sinc_function_1)))
fft_sinc_function_2 = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(sinc_function_2)))
fft_sinc_function_3 = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(sinc_function_3)))

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(3, 2, 1)
plt.imshow(sinc_function_1, extent=(-1, 1, -1, 1), cmap='viridis')
plt.title('F(f) = 2A sinc (2fA)')
plt.colorbar()

plt.subplot(3, 2, 2)
plt.imshow(np.abs(fft_sinc_function_1), cmap='viridis')
plt.title('2D FFT of F(f) = 2A sinc (2fA)')
plt.colorbar()

plt.subplot(3, 2, 3)
plt.imshow(sinc_function_2, extent=(-1, 1, -1, 1), cmap='viridis')
plt.title('F(f) = 2A sinc (2fA)')
plt.colorbar()

plt.subplot(3, 2, 4)
plt.imshow(np.abs(fft_sinc_function_2), cmap='viridis')
plt.title('2D FFT of F(f) = 2A sinc (2fA)')
plt.colorbar()

plt.subplot(3, 2, 5)
plt.imshow(sinc_function_3, extent=(-1, 1, -1, 1), cmap='viridis')
plt.title('F(f) = 6A sinc (6fA)')
plt.colorbar()

plt.subplot(3, 2, 6)
plt.imshow(np.abs(fft_sinc_function_3), cmap='viridis')
plt.title('2D FFT of F(f) = 6A sinc (6fA)')
plt.colorbar()

plt.tight_layout()
plt.show()
