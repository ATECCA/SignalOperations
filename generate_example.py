import os
import numpy as np
import matplotlib.pyplot as plt
from signal_ICT_KulangJamesGatgong_92400133006 import unit_step, unit_impulse, sine_wave, cosine_wave

# Make sure images/ exists
os.makedirs("images", exist_ok=True)

# 1. Unit Step
t = np.arange(-5, 6, 1)
x = unit_step(t)
plt.stem(t, x, use_line_collection=True)
plt.title("Unit Step Signal")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)
plt.savefig("images/unit_step.png")
plt.close()

# 2. Unit Impulse
x = unit_impulse(t)
plt.stem(t, x, use_line_collection=True)
plt.title("Unit Impulse Signal")
plt.xlabel("n")
plt.ylabel("δ[n]")
plt.grid(True)
plt.savefig("images/unit_impulse.png")
plt.close()

# 3. Sine Wave
t = np.linspace(0, 2*np.pi, 100)
x = sine_wave(amplitude=1, frequency=1, t=t)
plt.plot(t, x)
plt.title("Sine Wave")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid(True)
plt.savefig("images/sine_wave.png")
plt.close()

# 4. Cosine Wave
x = cosine_wave(amplitude=1, frequency=1, t=t)
plt.plot(t, x)
plt.title("Cosine Wave")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid(True)
plt.savefig("images/cosine_wave.png")
plt.close()

print("✅ All example plots saved in 'images/' folder!")
