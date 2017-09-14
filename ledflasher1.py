import time # for sleep function
import RPi.GPIO as GPIO #import the GPIO library

GPIO.setwarnings(False) # turn off warnings
GPIO.setmode(GPIO.BCM) # use board pin numbering on Pi Model 3

led_yellow = 21
led_red = 16
led_blue = 22
led_green = 18

GPIO.setup(led_yellow,GPIO.OUT) #setup GPIO pin to OUT
GPIO.setup(led_red,GPIO.OUT)
GPIO.setup(led_blue,GPIO.OUT)
GPIO.setup(led_green,GPIO.OUT)

time2sleep = 0.01


while True:
    GPIO.output(led_yellow,GPIO.HIGH)  # turns on GPIO pin
    time.sleep(time2sleep)
    GPIO.output(led_yellow,GPIO.LOW)
    time.sleep(time2sleep)
    GPIO.output(led_red,GPIO.HIGH)  
    time.sleep(time2sleep)
    GPIO.output(led_red,GPIO.LOW)
    time.sleep(time2sleep)
    GPIO.output(led_blue,GPIO.HIGH)  
    time.sleep(time2sleep)
    GPIO.output(led_blue,GPIO.LOW)
    time.sleep(time2sleep)
    GPIO.output(led_green,GPIO.HIGH)  
    time.sleep(time2sleep)
    GPIO.output(led_green,GPIO.LOW)
    time.sleep(time2sleep)
