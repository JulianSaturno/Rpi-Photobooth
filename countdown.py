import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
 
# GPIO ports for the 7seg pins
segments =  (17,27,22,5,6,13,26)
# 7seg_segment_pins (14,16,13,3,5,11,15) +  100R inline
 
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
 
# GPIO ports for the digit 0-3 pins 
digits = (23,24,25,12)
# 7seg_digit_pins (1,2,6,8) digits 0-3 respectively
 
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)
 
num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}
try:
    for x in range(1500):
#       n = time.ctime()[11:13]+time.ctime()[14:16]
        n = (x)  #Let x be any integer 0-9 for countdown sequence
        s = str(n).rjust(4)
        for digit in range(4):
            for loop in range(0,7):
                GPIO.output(segments[loop], num[s[digit]][loop])
#                if (int(time.ctime()[18:19])%2 == 0) and (digit == 1):
#                    GPIO.output(26, 1)
#                else:
#                    GPIO.output(26, 0)
            GPIO.output(digits[digit], 0)
            time.sleep(0.0001)
            GPIO.output(digits[digit], 1)
finally:
    GPIO.cleanup()
