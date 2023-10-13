import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Parameters
f_s = 44100  # Sampling frequency (standard for audio)
duration = 1  # Duration of the signal in seconds

# Generate rect(x) function signal for different intervals
def generate_rect_function(interval, T):
    t = np.linspace(0, duration, int(f_s * duration), endpoint=False)
    if interval == 1:
        rect_signal = np.where(np.logical_and(t >= -T/2, t <= T/2), 1.0, 0.0)
    elif interval == 2:
        rect_signal = np.where(np.logical_and(t >= -T, t <= T), 1.0, 0.0)
    elif interval == 3:
        rect_signal = np.where(np.logical_and(t >= -3*T, t <= 3*T), 1.0, 0.0)
    return rect_signal

# Define the intervals (in seconds)
intervals = [0.1, 0.2, 0.3]

# Create a collage of plots for each interval
plt.figure(figsize=(12, 9))

for idx, T in enumerate(intervals):
    rect_signal = generate_rect_function(idx+1, T)
    mfccs = librosa.feature.mfcc(y=rect_signal, sr=f_s, n_mfcc=13, n_fft=2048, hop_length=512)
    
    # Plot the rect(x) function signal
    plt.subplot(3, 2, 2*idx+1)
    plt.plot(rect_signal)
    plt.title(f'Rectangular Function Signal ({T}s Interval)')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    
    # Plot MFCC coefficients
    plt.subplot(3, 2, 2*idx+2)
    librosa.display.specshow(mfccs, x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title(f'MFCCs for Rectangular Function ({T}s Interval)')
    plt.xlabel('Time')
    plt.ylabel('MFCC Coefficient Index')

plt.tight_layout()
plt.show()
