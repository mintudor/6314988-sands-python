import matplotlib.pyplot as plt
from signals import create_sine_wave, create_step_signal, time_shift, time_scale

t1, y1 = create_sine_wave(frequency=5, duration=3)
t2, y2 = create_step_signal(duration=3)

t1_shifted, y1_shifted = time_shift(t1, y1, shift_amount=0.8)
t2_scaled, y2_scaled = time_scale(t2, y2, scale_factor=0.3)

print("Original sine wave:", (t1, y1))
print("Time-shifted sine wave:", (t1_shifted, y1_shifted))
print("Original step signal:", (t2, y2))
print("Time-shifted step signal:", (t2_scaled, y2_scaled))

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