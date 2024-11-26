# ISP

## Links and Resources

* [Arduino Reference](https://docs.arduino.cc/learn/programming/reference/)
* [Microsoft C++ Reference](https://learn.microsoft.com/en-us/cpp/cpp/cpp-language-reference?view=msvc-170)
 * [Raspberry Pi GPIO Reference](https://gpiozero.readthedocs.io)
* [Raspberry Pi Camera Reference](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)
* [Pyvesync Library](https://github.com/webdjoe/pyvesync)

## Ideas

* Solar panel that automatically points towards the sun
* Dice game using 7 Segment displays
* A true random number generator based on [Cloudflare's lava lamp wall](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)
* PC audio control board
* Trigger lights with Pi Camera using the [Pyvesync Library](https://github.com/webdjoe/pyvesync)
* Immersive backlighting based on [Govee's LED strips](https://us.govee.com/products/govee-gaming-light-strip-g1)

## Changelog
### 11/25/24
* Rewrote [Display](https://github.com/coollogan876/ISP/blob/main/Pi/Display.py) into a class
  * Allows making another display and configing pins simpler
### 11/24/24
* Added a ratchet sound to [Dice Display](https://github.com/coollogan876/ISP/blob/main/Pi/diceDisplay.py) using [Pygame Mixer](https://www.pygame.org/docs/ref/mixer.html)
* Changed [Dice Display](https://github.com/coollogan876/ISP/blob/main/Pi/diceDisplay.py) to use a forever loop instead of event handlers
  * Using event handlers allowed button spam/holding to unintentionally roll another random number
### 11/23/24
* Removed Signal.pause() from [Display](https://github.com/coollogan876/ISP/blob/main/Pi/Display.py)
  * [Dice Display](https://github.com/coollogan876/ISP/blob/main/Pi/diceDisplay.py) Would not run as it would run the pause command and not run anything else
  * 
## Author
- [Logan Dresel](https://www.github.com/coollogan876)
