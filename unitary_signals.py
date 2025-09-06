# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 10:55:05 2025

@author: Kulang James Gatgong
"""
import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    """Generates a unit step signal."""
    signal = np.heaviside(n, 1)
    plt.figure()
    plt.plot(n, signal, label='Unit Step Signal')
    plt.title('Unit Step Signal')
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.legend()
    plt.show()
    return signal

def unit_impulse(n):
    """Generates a unit impulse signal."""
    signal = np.zeros_like(n)
    if 0 in n:  # Check if zero is in the array
        signal[n == 0] = 1  # Impulse at n=0
    else:
        print("Warning: Zero is not in the input array, impulse signal will be empty.")
    plt.figure()
    plt.stem(n, signal, label='Unit Impulse Signal')  # Removed use_line_collection
    plt.title('Unit Impulse Signal')
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.legend()
    plt.show()
    return signal


def ramp_signal(n):
    """Generates a ramp signal."""
    signal = np.maximum(0, n)  # Ramp starts at 0
    plt.figure()
    plt.plot(n, signal, label='Ramp Signal')
    plt.title('Ramp Signal')
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.legend()
    plt.show()
    return signal

# Example usage
n = np.arange(-5, 6, 1)  # Define a range for n
unit_step(n)
unit_impulse(n)
ramp_signal(n)
