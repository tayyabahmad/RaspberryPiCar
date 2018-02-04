import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(16, gpio.OUT)

gpio.output(11, 0)
gpio.output(13, 0)
gpio.output(15, 0)
gpio.output(16, 0)
gpio.cleanup()


