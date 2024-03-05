import RPi.GPIO as gpio
import time

led=26

gpio.setmode(gpio.BCM)

gpio.setup(led, gpio.OUT)
try:
    while True:
        gpio.output(led, gpio.HIGH)
        time.sleep(1)
        gpio.output(led, gpio.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    pass

gpio.cleanup()