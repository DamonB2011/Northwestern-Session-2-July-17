import board
import time
import pwmio  # get access to PWM
from analogio import AnalogIn  # get access to analog pins
import digitalio

potentiometerpin = AnalogIn(board.A0)  # on the Pico there are only 3 pins that can do this!

led = pwmio.PWMOut(board.GP14, variable_frequency=True)
led.duty_cycle = 0  # initially off, 16 bit number so max on is 65535

buttonpin = digitalio.DigitalInOut(board.GP15)
buttonpin.direction = digitalio.Direction.INPUT

while True:
    if buttonpin.value == 0:  # if the button is pressed
        knobValue = potentiometerpin.value  # analog converter returns 0 for 0V, 65535 for 3.3V
        led.duty_cycle = knobValue
        print(str(round((knobValue / 65535) * 100, 2)) + "% brightness")
    time.sleep(0.1)  # update 10 times per second
