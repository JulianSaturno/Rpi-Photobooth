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
