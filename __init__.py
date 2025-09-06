# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 10:54:37 2025

@author: Kulang James Gatgong
"""

# __init__.py

# Define the version of the package
__version__ = '0.1.0'

# Import specific functions or classes to make them available at the package level
from .unitary_signals import unit_step, unit_impulse
from .trigonometric_signals import sine_wave, cosine_wave

# Optionally, define an __all__ list to control what is imported with *
__all__ = ['unit_step', 'unit_impulse', 'sine_wave', 'cosine_wave']
