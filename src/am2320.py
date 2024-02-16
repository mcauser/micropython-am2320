# SPDX-FileCopyrightText: 2016 Mike Causer <https://github.com/mcauser>
# SPDX-License-Identifier: MIT

"""
MicroPython Aosong AM2320 I2C driver
https://github.com/mcauser/micropython-am2320
"""

from time import sleep_ms
from micropython import const

__version__ = "1.1.0"

I2C_ADDRESS = const(0x5C)  # fixed I2C address


class AM2320:
    def __init__(self, i2c):
        self._i2c = i2c
        self._buf = bytearray(8)

    def check(self):
        self._wake()
        if self._i2c.scan().count(I2C_ADDRESS) == 0:
            raise OSError(f"AM2320 not found at I2C address {I2C_ADDRESS:#x}")
        return True

    def measure(self):
        buf = self._buf
        # wake sensor
        self._wake()
        # read 4 registers starting at offset 0x00
        self._i2c.writeto(I2C_ADDRESS, b"\x03\x00\x04")
        # wait at least 1.5ms
        sleep_ms(2)
        # read data
        self._i2c.readfrom_mem_into(I2C_ADDRESS, 0, buf)
        crc = buf[6] | (buf[7] << 8)
        if crc != self._crc16(buf[:-2]):
            raise ValueError("Checksum error")

    def temperature(self):
        t = ((self._buf[4] & 0x7F) << 8 | self._buf[5]) * 0.1
        if self._buf[4] & 0x80:
            t = -t
        return t

    def humidity(self):
        return (self._buf[2] << 8 | self._buf[3]) * 0.1

    def _wake(self):
        try:
            self._i2c.writeto(I2C_ADDRESS, b"")
        except OSError:
            pass
        sleep_ms(10)

    def _crc16(self, buf):
        crc = 0xFFFF
        for c in buf:
            crc ^= c
            for _ in range(8):
                if crc & 0x01:
                    crc >>= 1
                    crc ^= 0xA001
                else:
                    crc >>= 1
        return crc
