# code modified, tweaked and tailored from code by bertwert 
# on RPi forum thread topic 91796
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

def number3():
    try:
        for x in range(1500):
    #       n = time.ctime()[11:13]+time.ctime()[14:16]
            n = (3)
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

def number2():
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
            n = (2)
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

def number1():
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
            n = (1)
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

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from picamera import PiCamera
import time

camera = PiCamera() 
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering


def cheese():
    global camera
    camera.rotation = 180
    camera.start_preview(alpha=200)

    for i in range(0,4,1):
        time.sleep(2)
        camera.capture('/home/saturnojulia/Python/Photobooth_Photos/image%s.jpg' % i)
        
    camera.stop_preview()
    
def stitch():
    from PIL import Image
    Image01 = Image.open("/home/saturnojulia/Python/Photobooth_Photos/image0.jpg").resize((450,450))
    Image02 = Image.open("/home/saturnojulia/Python/Photobooth_Photos/image1.jpg").resize((450,450))
    Image03 = Image.open("/home/saturnojulia/Python/Photobooth_Photos/image2.jpg").resize((450,450))
    Image04 = Image.open("/home/saturnojulia/Python/Photobooth_Photos/image3.jpg").resize((450,450))
    Logo = Image.open("/home/saturnojulia/Desktop/SuLogo.png")
    Logo = Logo.resize((200,200))

    newImage = Image.new("RGB", (2000, 500), (0, 0, 0) )

    newImage.paste(Image01,(25,25))
    newImage.paste(Image02,(475,25))
    newImage.paste(Image03,(925,25))
    newImage.paste(Image04,(1375,25))

    newImage.paste(Logo,(1800,300))

    newImage.save("/home/saturnojulia/Python/Photobooth_Photos/Saved.jpg")
    
def tweet():
    from twython import Twython 
    # Fill in your keys and token infollowing variables 
    C_key = "Secret" 
    C_secret = "Secret" 
    A_token = "Secret" 
    A_secret = "Secret" 

    # Authenticate to your app.
    twitter = Twython(C_key,C_secret,A_token,A_secret) 

    # Tweet text by editing the text in the quotes. 
    twitter.update_status(status = input("Introduce your tweet: "))

    # Tweet Photos 
    photo = open('/home/saturnojulia/Python/Photobooth_Photos/Saved.jpg', 'rb') 
    response = twitter.upload_media(media=photo)
    twitter.update_status(status = input("Caption your tweet: "), media_ids=[response['media_id']])

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 16 to be an input pin and set initial value to be pulled low (off)  

ok2run = True
def button_callback(channel):
    global ok2run
    if ok2run == True:
        number3()
        number2()
        number1()
        cheese()
        stitch()
        tweet()
    
GPIO.setwarnings(False)

GPIO.add_event_detect(16,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

try:
    while(1):
        time.sleep(1e6)
finally:
    GPIO.cleanup() # Clean up
