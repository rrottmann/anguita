#!/usr/bin/env python

from setuptools import setup

setup(
    name='anguita',
    version='0.1',
    description='Fast approximation of tanh with good enough results.',
    author='Reiner Rottmann',
    author_email='reiner@rottmann.it',
    url='https://github.com/rrottmann/anguita',
    packages=['anguita'],
    long_description="""\
    Efficient tanh algorithm using an approximation of the Hyperbolic function:
    Speed Improvement of the Back-Propagation on Current Generation
    Workstations" D. Anguita, G. Parodi and R. Zunino. Proceedings of the World
    Congress on Neural Networking, 1993.
    """,
    classifiers=[
          'License :: OSI Approved :: MIT License',
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: Internet",
    ],
    keywords='neural network, tanh, math',
    license='MIT License, see LICENSE',
    install_requires=[ 'setuptools']
)
