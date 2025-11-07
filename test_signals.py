from signals import create_sine_wave, create_step_signal, time_shift, time_scale

t, y = create_sine_wave(2, 1)
print("Sine Wave:", t[:5], y[:5])

t_step, y_step = create_step_signal(1)
print("Step Signal:", t_step[:5], y_step[:5])

t_shifted, y_shifted = time_shift(t, y, 0.1)
print("Shifted Sine Wave:", t_shifted[:5], y_shifted[:5])

t_scaled, y_scaled = time_scale(t_step, y_step, 0.5)
print("Scaled Step Signal:", t_scaled[:5], y_scaled[:5])