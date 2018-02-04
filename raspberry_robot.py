from socket import *
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)  # motor 2
    GPIO.setup(13, GPIO.OUT)  # motor 2
    GPIO.setup(15, GPIO.OUT)  # motor 1
    GPIO.setup(16, GPIO.OUT)  # motor 1
    GPIO.setup(36, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)  # enable 2
GPIO.setup(36, GPIO.OUT)  # enable 1

GPIO.output(36, True)  # enable 1
GPIO.output(37, True)  # enable 2

state = True

HOST = "192.168.0.107"  # local host
PORT = 9000  # open port 7000 for connection
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)  # how many connections can it receive at one time
conn, addr = s.accept()  # accept the connection
print "Connected by: ", addr  # print the address of the person connected
while True:
    data = conn.recv(1024)  # how many bytes of data will the server receive

    my_data= data.rstrip()
    print ('data is: ',my_data)
    if my_data == 'u':
        init()
        GPIO.output(11, True)
        GPIO.output(13, False)
        GPIO.output(15, True)
        GPIO.output(16, False)
        print 'forward'
        #GPIO.cleanup()

    elif my_data == 'l':
        init()
        print 'left'
        GPIO.output(11, True)
        GPIO.output(13, True)
        GPIO.output(15, True)
        GPIO.output(16, False)
        #GPIO.cleanup()

    elif my_data == 'r':
        init()
        print 'right'
        GPIO.output(11, True)
        GPIO.output(13, False)
        GPIO.output(15, True)
        GPIO.output(16, True)
        #GPIO.cleanup()

    elif my_data == 'd':
        init()
        print 'reverse'
        GPIO.output(11, False)
        GPIO.output(13, True)
        GPIO.output(15, False)
        GPIO.output(16, True)
        #GPIO.cleanup()
    else :
        init()
        print 'stop'
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        GPIO.output(16, False)
        #GPIO.cleanup()

    print "Received: ", repr(data)
# reply = raw_input("Reply: ") #server's reply to the client
    reply = ("ok")
    conn.sendall(reply)
conn.close()
