# Raspberry Pi Photobooth
- Because taking selfies with your phone is too mainstream.

## Inspiration

Many of us have the need to receive self-validation from aquaintences online but are sick of routinely taking the same photos on their cellular device.  We decided to create a DIY photobooth so you can strut your stuff in front of your Raspberry Pi.

In the US alone, over 93 million selfies are taken and uploaded to the internet sphere, predominely on Instragram and Twitter.  But, just how long does it take to effectively undergo such an integral process in the teenage life?  How can we effictively reduce the amount of time it takes to upload our selfies? 

## What it does
Upon pressing a push button, the Raspberry Pi should take four photos with a set delay between them, concatenate them horizontally, put a border with a Seattle U logo around them, and tweet it.  There should also be a four-digit seven-segment LED display that counts down between the photos.

Process:
- Set up a push-button with a pullup resistor to avoid overloading the Pi's 3.3v GPIO limit

![Step 1](https://github.com/JulianSaturno/RPi-Photobooth/blob/master/images/pushbutton.PNG)

- Attach the Pi-Camera to the Raspberry Pi and allow for Camera use in raspiconfig

![Step 2](https://github.com/JulianSaturno/RPi-Photobooth/blob/master/images/picamera.png)

- With the implementation of a libary, where the ones represent a segment of the display, we can call a for loop to flash a number of our choosing for a certain amount of time

![Step 3](https://github.com/JulianSaturno/RPi-Photobooth/blob/master/images/segment.png)

- The final product 

![Step 4](https://github.com/JulianSaturno/RPi-Photobooth/blob/master/images/final-product.png)

- Firing the new machine gives us a nice Twitter post with our collage of photos and a collegiate logo

![Step 5](https://github.com/JulianSaturno/RPi-Photobooth/blob/master/images/twitterpost.png)
