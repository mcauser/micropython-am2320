# AM2320 I2C

A MicroPython library for interfacing with an Aosong AM2320 temperature and humidity sensor over I2C.

This library focuses on using the I2C interface. The sensor also supports a 1-wire interface, available when pin 4 is connected to GND.

#### Pinout

```
+---------+
|xxxxxxxxx|
|xxxxxxxxx|
|xxxxxxxxx|
|xxxxxxxxx|
|xxxxxxxxx|
+---------+
  | | | |
  1 2 3 4
```

1=VDD, 2=SDA, 3=GND, 4=SCL

For full documentation see http://micropython-am2320.rtfd.io/.

![demo](docs/AM2320.jpg)