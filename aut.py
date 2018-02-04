import RPi.GPIO as gpio
import time
import sys
import random

gpio.setmode(gpio.BOARD)
TRIG = 40
ECHO = 38

gpio.setup(TRIG, gpio.OUT)
gpio.setup(ECHO, gpio.IN)

def init():
    print 'stop'
    gpio.setmode(gpio.BOARD)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(16, gpio.OUT)
    gpio.setwarnings(False)

def forward():
    init()
    print 'forward'
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(16, False)
    gpio.cleanup()

def reverse():
    init()
    print 'reverse'
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(16, True)
    gpio.cleanup()

def turn_left():
    init()
    print 'left'
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(16, False)
    gpio.cleanup()

def turn_right():
    init()
    print 'right'
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(16, True)
    gpio.cleanup()


init()
count=0
while True:
  i=0
  avgDistance=0
  for i in range(5):
      gpio.setmode(gpio.BOARD)
      TRIG = 40
      ECHO = 38

      gpio.setup(TRIG, gpio.OUT)
      gpio.setup(ECHO, gpio.IN)
      gpio.output(TRIG, False)                 #Set TRIG as LOW
      time.sleep(0.1)                                   #Delay

      gpio.output(TRIG, True)                  #Set TRIG as HIGH
      time.sleep(0.00001)                           #Delay of 0.00001 seconds
      gpio.output(TRIG, False)                 #Set TRIG as LOW

      while gpio.input(ECHO)==0:              #Check whether the ECHO is LOW
        pulse_start = time.time()

      while gpio.input(ECHO)==1:              #Check whether the ECHO is HIGH
        pulse_end = time.time()
      
      pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor

      distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
      distance = round(distance,2)                 #Round to two decimal points
      avgDistance=avgDistance+distance

      avgDistance=avgDistance/5
      print avgDistance
      flag=0
      if avgDistance < 15:      #Check whether the distance is within 15 cm range
          count=count+1
          init()
          time.sleep(1)
          reverse()
          time.sleep(1.5)
          if (count%3 ==1) & (flag==0):
              turn_right()
              flag=1
          else:
              turn_left()
              flag=0
              time.sleep(1.5)
              init()
              time.sleep(1)

      else:
          forward()
          flag =0
