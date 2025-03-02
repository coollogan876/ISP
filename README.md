# ISP

## Links and Resources

* [Arduino Reference](https://docs.arduino.cc/learn/programming/reference/)
* [Microsoft C++ Reference](https://learn.microsoft.com/en-us/cpp/cpp/cpp-language-reference?view=msvc-170)
 * [Raspberry Pi GPIO Reference](https://gpiozero.readthedocs.io)
* [Raspberry Pi Camera Reference](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)
* [Pyvesync Library](https://github.com/webdjoe/pyvesync)
* [Scikit Image Processing Reference](https://scikit-image.org/docs/stable/api/api.html)

## Ideas

* Solar panel that automatically points towards the sun
* Dice game using 7 Segment displays
* A true random number generator based on [Cloudflare's lava lamp wall](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)
* PC audio control board
* Trigger lights with Pi Camera using the [Pyvesync Library](https://github.com/webdjoe/pyvesync)
* Immersive backlighting based on [Govee's LED strips](https://us.govee.com/products/govee-gaming-light-strip-g1)
* Motion detection using [Scikit Image Processing](https://scikit-image.org/)

## Changelog
### 12/5/24
* Implemented the [Mersenne Twister method](https://www.sciencedirect.com/topics/computer-science/mersenne-twister) into the [seed generator](https://github.com/coollogan876/ISP/blob/main/Pi/TrueRandom/Seed.py) for better randomness
* Fixed some errors in the [seed generator](https://github.com/coollogan876/ISP/blob/main/Pi/TrueRandom/Seed.py) and in the [random methods](https://github.com/coollogan876/ISP/blob/main/Pi/TrueRandom/TrueRandom.py)
  * Python does not allow overloading methods like other languages do.
  In order to allow different parameters to be used, use var=None
  * Some variables in the [seed generator](https://github.com/coollogan876/ISP/blob/main/Pi/TrueRandom/Seed.py) that have bitwise operators applied to them can throw an error about it not being type safe. To prevent this use int() to make sure it doesn't throw an error.
* Managed to generate a random password using blob detection of a lava lamp: KnDTj$Gby%*laKQizDZs
 According to [security.org](https://www.security.org/how-secure-is-my-password/) It would take approximately 2 quintillion years to crack
### 12/3/24
* Started working on [a true random number generator](https://github.com/coollogan876/ISP/tree/main/Pi) based on [Cloudflare's lava lamp wall](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/) used to create encryption keys
### 12/2/24 
* Created [Motion Detection](https://github.com/coollogan876/ISP/blob/main/Pi/MotionDetection.py) 
  * Using [Scikit Image Processing](https://scikit-image.org/)
### 11/30/24
* Added a second display to [Dice Display](https://github.com/coollogan876/ISP/blob/main/Pi/diceDisplay.py) 
  * The code now generates a random number between 0 and 12 and displays it on both screens
### 11/25/24
* Rewrote [Display](https://github.com/coollogan876/ISP/blob/main/Pi/Display.py) into a class
  * Allows making another display and configuring pins simpler
### 11/24/24
* Added a ratchet sound to [Dice Display](https://github.com/coollogan876/ISP/blob/main/Pi/diceDisplay.py) using [Pygame Mixer](https://www.pygame.org/docs/ref/mixer.html)
* Changed [Dice Display](https://github.com/coollogan876/ISP/blob/main/Pi/diceDisplay.py) to use a forever loop instead of event handlers
  * Using event handlers allowed button spam/holding to unintentionally roll another random number
### 11/23/24
* Removed Signal.pause() from [Display](https://github.com/coollogan876/ISP/blob/main/Pi/Display.py)
  * [Dice Display](https://github.com/coollogan876/ISP/blob/main/Pi/diceDisplay.py) would not run as it would run the pause command and not run anything else
## Author
- [Logan Dresel](https://www.github.com/coollogan876)
