# SPDX-FileCopyrightText: 2016 Mike Causer <https://github.com/mcauser>
# SPDX-License-Identifier: MIT

"""
MicroPython Aosong AM2320 I2C driver
https://github.com/mcauser/micropython-am2320

Prints the temperature and humidity
"""

from machine import I2C, Pin
import am2320

i2c = I2C(0)
sensor = am2320.AM2320(i2c)

if sensor.check():
    print(f"AM2320 found at I2C address {am2320.I2C_ADDRESS:#x}")

sensor.measure()
print(f"Temperature: {sensor.temperature()} C")
print(f"Humidity: {sensor.humidity()} RH")
