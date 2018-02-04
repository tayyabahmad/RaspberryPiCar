import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

ECHO = 38
TRIG = 40

print 'Distance measuring in process'

gpio.setup(TRIG, gpio.OUT)
gpio.setup(ECHO, gpio.IN)

gpio.output(TRIG, False)
print 'please wait. .'
time.sleep(2)

gpio.output(TRIG, True)
time.sleep(0.00001)
gpio.output(TRIG, False)

while gpio.input(ECHO) == 0:
  start = time.time()

while gpio.input(ECHO) == 1:
  end = time.time()

duration = end - start
distance = duration / 0.000058

distance = round(distance, 2)
print 'distance: ', distance,'cm'

gpio.cleanup()


