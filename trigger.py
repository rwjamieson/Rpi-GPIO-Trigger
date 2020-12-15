#!/usr/bin/env python
from time import sleep
import RPi.GPIO as GPIO
i = 0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

GPIO.output(21, True)
sleep(0.3)
GPIO.output(21, False)
sleep(0.1)