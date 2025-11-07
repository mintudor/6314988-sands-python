import numpy as np
import matplotlib.pyplot as plt

def create_sine_wave(frequency, duration, sampling_rate=44100):
  t = np.linspace(0, duration, int(sampling_rate * duration))
  y = np.sin(2 * np.pi * frequency * t)
  return t, y

def create_step_signal(duration, sampling_rate=44100):
  t = np.linspace(0, duration, int(sampling_rate * duration))
  y= np.ones_like(t)
  y[int(len(y)/2):]=0
  return t,y

def time_shift(t, y, shift_amount):
  return t + shift_amount, y

def time_scale(t, y, scale_factor):
  return t * scale_factor, y
 
t1, y1 = create_sine_wave(frequency=2, duration=2)
t2, y2 = create_step_signal(duration=2)

t1_shifted, y1_shifted = time_shift(t1, y1, shift_amount=0.5)
t2_scaled, y2_scaled = time_scale(t2, y2, scale_factor=0.5)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(t1, y1)
plt.title("Original Sine Wave")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.subplot(2, 2, 2)
plt.plot(t1_shifted, y1_shifted)
plt.title("Time-Shifted Sine Wave")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.subplot(2, 2, 3)
plt.plot(t2 ,y2)
plt.title("Original Step Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.subplot(2, 2, 4)
plt.plot(t2_scaled ,y2_scaled)
plt.title("Time-Scaled Step Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show() 
