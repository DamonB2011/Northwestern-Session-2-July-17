import board  # the pin definitions
import time
import digitalio  # get access to digital pins

# make pin GP14 a digital output
greenled = digitalio.DigitalInOut(board.GP14)
greenled.direction = digitalio.Direction.OUTPUT

morseCodeInput = "-- --- .-. ... . / -.-. --- -.. ."  # placeholder message pattern

dit = 0.2  # in seconds
dah = 3 * dit
pauseBetweenFlash = dit
pauseBetweenLetter = dit * 3
pauseBetweenWord = dit * 7
pauseBetweenRepeat = dit * 10

while True:
    for char in morseCodeInput:
        greenled.value = 1  # turn on the led
        if char == ".":
            time.sleep(dit)
        if char == "-":
            time.sleep(dah)
        greenled.value = 0
        if char == " ":  # if there is a space meaning new letter
            time.sleep(pauseBetweenLetter)
        elif char == "/":  # if there is a space between words
            time.sleep(pauseBetweenWord)
        else:
            time.sleep(pauseBetweenFlash)  # wait before going to the next character
    time.sleep(pauseBetweenRepeat)  # pause for a bit between loops
