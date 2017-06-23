import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup

setup(
    name='micropython-am2320',
    py_modules=['am2320'],
    version='1.0.0',
    description='MicroPython library for the AM2320 temperature and humidity sensor.',
    long_description='This library lets you communicate with an Aosong AM2320 temperature and humidity sensor over I2C.',
    keywords='am2320 aosong dht temperature humidity micropython',
    url='https://github.com/mcauser/micropython-am2320',
    author='Mike Causer',
    author_email='mcauser@gmail.com',
    maintainer='Mike Causer',
    maintainer_email='mcauser@gmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: OSI Approved :: MIT License',
    ],
)