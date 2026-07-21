import board
import time
import digitalio

# an LED on GP14, set as an output pin
greenled = digitalio.DigitalInOut(board.GP14)
greenled.direction = digitalio.Direction.OUTPUT

# a push button circuit on GP15, set as an input pin
buttonpin = digitalio.DigitalInOut(board.GP15)
buttonpin.direction = digitalio.Direction.INPUT

count = 0
canAdd = True

while True:
    if buttonpin.value == 0:  # if you're holding down the button
        greenled.value = 1  # turn on the light
        if canAdd:
            canAdd = False  # prevent continuous incrementation
            count = count + 1
            print(count)
    else:
        greenled.value = 0
        canAdd = True  # once released, allow count to be incremented again
    # if printing, slow down the code to less than 100Hz
    # or your computer screen will struggle to show all the prints
    time.sleep(0.05)  # 20 times per second
