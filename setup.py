# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 15:23:02 2025

@author: Kulang James Gatgong
"""

from setuptools import setup, find_packages

setup(
    name='signal_ICT_KulangJamesGatgong_92400133006',
    version='0.1.0',
    author='Kulang James Gatgong',
    author_email='kulangjamesgatgong.124189@marwadiuniversity.ac.in',
    description='A package for signal processing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourrepository',
    packages=find_packages(),
    install_requires=[
        'numpy',  # For numerical operations
        'matplotlib',  # For plotting
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',
)
