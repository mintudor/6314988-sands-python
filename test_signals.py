import numpy as np
import pytest
from signals import create_sine_wave, create_step_signal, time_shift, time_scale

def test_create_sine_wave():
    """Check sine wave length and basic values."""
    t, y = create_sine_wave(2, 1)
    assert len(t) == len(y)
    assert y[0] == pytest.approx(0, abs=1e-8)

def test_create_step_signal():
    """Check step signal is 1 in first half and 0 in second half."""
    t, y = create_step_signal(1)
    half = len(y) // 2
    assert np.all(y[:half] == 1)
    assert np.all(y[half:] == 0)

def test_time_shift():
    """Check time shift moves t but leaves y unchanged."""
    t, y = create_sine_wave(1, 1)
    shift_amount = 0.1
    t_shifted, y_shifted = time_shift(t, y, shift_amount)
    assert np.all(y_shifted == y)
    assert t_shifted[0] == pytest.approx(t[0] + shift_amount)

def test_time_scale():
    """Check time scaling multiplies t but leaves y unchanged."""
    t, y = create_step_signal(1)
    scale_factor = 0.5
    t_scaled, y_scaled = time_scale(t, y, scale_factor)
    assert np.all(y_scaled == y)
    assert t_scaled[1] == pytest.approx(t[1] * scale_factor)
