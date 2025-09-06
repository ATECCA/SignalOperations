# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 15:23:02 2025
@author: Kulang James Gatgong
"""

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='signal_ICT_KulangJamesGatgong_92400133006',
    version='0.1.0',
    author='Kulang James Gatgong',
    author_email='kulangjamesgatgong.124189@marwadiuniversity.ac.in',
    description='A package for signal processing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ATECCA/SignalOperations',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',
)
