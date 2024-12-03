# ISP

## Links and Resources

* [Arduino Reference](https://docs.arduino.cc/learn/programming/reference/)
* [Microsoft C++ Reference](https://learn.microsoft.com/en-us/cpp/cpp/cpp-language-reference?view=msvc-170)
 * [Raspberry Pi GPIO Reference](https://gpiozero.readthedocs.io)
* [Raspberry Pi Camera Reference](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)
* [Pyvesync Library](https://github.com/webdjoe/pyvesync)
* [Scikit Image Processing Reference](https://scikit-image.org/docs/stable/api/api.html)
* [Open CV2 Reference](https://docs.opencv.org/4.x/index.html)

## Ideas

* Solar panel that automatically points towards the sun
* Dice game using 7 Segment displays
* A true random number generator based on [Cloudflare's lava lamp wall](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)
* PC audio control board
* Trigger lights with Pi Camera using the [Pyvesync Library](https://github.com/webdjoe/pyvesync)
* Immersive backlighting based on [Govee's LED strips](https://us.govee.com/products/govee-gaming-light-strip-g1)
* Motion detection using [Scikit Image Processing](https://scikit-image.org/)

## Changelog
### 12/2/24
* Created [Motion Detection](https://github.com/coollogan876/ISP/blob/main/Pi/MotionDetection.py) 
  * Using [Open CV2](https://docs.opencv.org/4.x/index.html) to compare the similarity of 2 separate images taken by the Pi Camera and turn on a smart plug through the [Pyvesync Library](https://github.com/webdjoe/pyvesync)
### 11/30/24
* Added a second display to [Dice Display](https://github.com/coollogan876/ISP/blob/main/Pi/diceDisplay.py) 
  * The code now generates a random number between 0 and 12 and displays it on both screens
### 11/25/24
* Rewrote [Display](https://github.com/coollogan876/ISP/blob/main/Pi/Display.py) into a class
  * Allows making another display and configing pins simpler
### 11/24/24
* Added a ratchet sound to [Dice Display](https://github.com/coollogan876/ISP/blob/main/Pi/diceDisplay.py) using [Pygame Mixer](https://www.pygame.org/docs/ref/mixer.html)
* Changed [Dice Display](https://github.com/coollogan876/ISP/blob/main/Pi/diceDisplay.py) to use a forever loop instead of event handlers
  * Using event handlers allowed button spam/holding to unintentionally roll another random number
### 11/23/24
* Removed Signal.pause() from [Display](https://github.com/coollogan876/ISP/blob/main/Pi/Display.py)
  * [Dice Display](https://github.com/coollogan876/ISP/blob/main/Pi/diceDisplay.py) would not run as it would run the pause command and not run anything else
## Author
- [Logan Dresel](https://www.github.com/coollogan876)
