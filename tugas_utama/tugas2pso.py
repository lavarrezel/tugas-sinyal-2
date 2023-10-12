import numpy as np
def convolve(x, y):
   
    if not isinstance(x, list) or not isinstance(y, list):
        raise ValueError("Sinyal harus 1 dimensi.")

    n = len(x) + len(y) - 1

    z = [0] * n

    for i in range(n):
        for j in range(len(x)):
            if i - j >= 0 and i - j < len(y):
                z[i] += x[j] * y[i - j]

    return z

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
z = convolve(x, y)
z_numpy = np.convolve(x, y)

assert np.allclose(z, z_numpy)

print("Nama : Alfa Naufal Afif Lintang Madani")
print("NRP : 5009211062")
