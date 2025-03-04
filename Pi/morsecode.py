'''
Morse code generator
'''
from gpiozero import LED
from time import sleep
from signal import pause

led = LED(2)
led.on()
sleep(.5)
led.off()

alphabet = {
        "a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", 'f':'..-.', 'g':'--.',
        'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.',
        'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-',
        'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', '1':'.----',
        '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
        '8':'---..', '9':'----.', '0':'-----', ' ':' '}

untranslatedString = input('Enter text to turn into morse code: ')
translatedString = "";

for character in untranslatedString:
    character.lower()
    translatedString += alphabet[character]

print(untranslatedString + '\ntranslates to\n' + translatedString)

for character in translatedString:
    if character == '.':
        led.on()
        sleep(.25)
        led.off()
    elif character == '-':
        led.on()
        sleep(.5)
        led.off()
    else:
        sleep(.5)

pause()

