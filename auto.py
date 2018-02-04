import RPi.GPIO as gpio
import time
import sys
import random

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(16, gpio.OUT)
    gpio.setwarnings(False)

def forward(tf):
    init()
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(16, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(16, True)
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    init()
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(16, False)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    init()
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(16, True)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    init()
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(16, False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    init()
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(16, True)
    time.sleep(tf)
    gpio.cleanup()

def distance():
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
    time.sleep(1)

    gpio.output(TRIG, True)
    time.sleep(0.00001)
    gpio.output(TRIG, False)

    while gpio.input(ECHO) == 0:
      start = time.time()

    while gpio.input(ECHO) == 1:
      end = time.time()

    duration = end - start
    distance = duration / 0.000058

    print 'distance: ', distance,'cm'

    return distance
    gpio.cleanup()

def auto():
    dist = distance()
    if dist < 20:
        reverse(2)

def check_front():
    init()
    dist = distance()

    if dist < 15:
        print('too close', dist)
        init()
        print'now moving in reverse direction'
        reverse(2)
        dist = distance()

        if dist < 15:
            print('Too close', dist)
            init()
            print'pivot to the left'
            pivot_left(3)
            init()
            print'now moving in reverse'
            reverse(2)
            dist = distance()
            if dist < 15:
                print('Too close', dist)
                init()
                print'pivot to the left'
                pivot_left(3)
                init()
                print'now moving in reverse'
                reverse(2)
                dist = distance()

                if dist < 15:
                    print('still too close! exiting', dist)
                    sys.exit()
def autonomy():
    tf = 0.030
    x = random.randrange(0,4)

    if x == 0:
        for y in range(30):
            check_front()
            print'forward direction'
            init()
            forward(tf)
    elif x == 1:
        for y in range(30):
            check_front()
            print'pivot left'
            init()
            pivot_left(tf)
    elif x == 2:
         for y in range(30):
            check_front()
            print'moving to right'
            init()
            turn_right(tf)
    elif x == 3:
        for y in range(30):
            check_front()
            print'turning to the left'
            init()
            turn_left(tf)

for z in range(10):
    autonomy()
