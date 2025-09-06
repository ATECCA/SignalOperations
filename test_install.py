# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 16:05:54 2025

@author: Kulang James Gatgong
"""

import numpy as np
import signal_ict_Kulang_James_Gatgong_92400133006 as sik  

print("===== Testing signal_ict_Seshu_Vardhan_Reddy package =====")

n = np.arange(10)
t = np.linspace(0, 1, 100)

# 1. Unit Step
print("Unit Step:", sik.unit_step(n))

# 2. Unit Impulse
print("Unit Impulse:", sik.unit_impulse(n))

# 3. Ramp Signal
print("Ramp Signal:", sik.ramp_signal(n))

# 4. Sine Wave
sine = sik.sine_wave(1, 5, 0, t)
print("Sine Wave (first 10 values):", sine[:10])

# 5. Cosine Wave
cosine = sik.cosine_wave(1, 5, 0, t)
print("Cosine Wave (first 10 values):", cosine[:10])

# 6. Exponential Signal
exp_signal = sik.exponential_signal(n, a=0.2)
print("Exponential Signal:", exp_signal)

# 7. Time Shift
sine_shifted = sik.time_shift(sine, 5)
print("Time Shifted Sine (first 10 values):", sine_shifted[:10])

# 8. Time Scale
sine_scaled = sik.time_scale(sine, 2)
print("Time Scaled Sine (first 10 values):", sine_scaled[:10])

# 9. Signal Addition
added = sik.signal_addition(sik.unit_step(n), sik.ramp_signal(n))
print("Signal Addition (Step + Ramp):", added)

# 10. Signal Multiplication
multiplied = sik.signal_multiplication(sine, cosine)
print("Signal Multiplication (first 10 values):", multiplied[:10])

