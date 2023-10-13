
import numpy as np
import matplotlib.pyplot as plt

# Define the fourier sinc function with parameters n and A
def fourier_sinc(f, A, n):
    # Return the product of n, A and the sinc function of f times A
    return n * A * np.sinc(n * A * f)

# Create an array of f values from -5 to 5 with 0.01 intervals
f = np.arange(-8, 8, 0.01)

# Choose some values for n and A
n = 2
A = 1

# Apply the fourier sinc function to the f values and store the result in F
F = fourier_sinc(f, A, n)

# Plot the f and F values using a blue line
plt.plot(f, F, 'b-')

# Add labels and title to the plot
plt.xlabel('f')
plt.ylabel('F(f)')
plt.title('Fourier Sinc Function F(f) = nA sinc (nfA)')

# Show the plot
plt.show()
