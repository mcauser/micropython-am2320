Usage Examples
**************

Connect your sensor in following way:

    * ``vin`` ↔ ``3V``
    * ``sda`` ↔ ``gpio4``
    * ``gnd`` ↔ ``gnd``
    * ``scl`` ↔ ``gpio5``

Now, to make basic measurement::

    import am2320
    from machine import I2C, Pin
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    sensor = am2320.AM2320(i2c)
    sensor.measure()
    print(sensor.temperature())
    print(sensor.humidity())

To perform continuous measurement::

    import time
    while True:
        sensor.measure()
        print(sensor.temperature())
        print(sensor.humidity())
        time.sleep_ms(4000)
