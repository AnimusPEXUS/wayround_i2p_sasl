#!/usr/bin/python3

from setuptools import setup

setup(
    name='wayround_i2p_sasl',
    version='0.1',
    description='pure python sasl mechanisms realisation',
    author='Alexey Gorshkov',
    author_email='animus@wayround.org',
    url='https://github.com/AnimusPEXUS/wayround_i2p_sasl',
    install_requires=[
        ],
    packages=[
        'wayround_i2p.sasl'
        ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
        ]
    )
