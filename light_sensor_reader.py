import board
import time
from analogio import AnalogIn  # get access to analog pins

lightSensorPin = AnalogIn(board.A0)  # on the Pico there are only 3 pins that can do this!

while True:
    rawValue = lightSensorPin.value  # analog converter returns 0 for 0V, 65535 for 3.3V
    volts = 3.3 * rawValue / 65535
    percentValue = rawValue / 65535 * 100
    print(str(round(percentValue, 1)) + "%, " + str(round(volts, 2)) + " volts")
    time.sleep(0.1)  # update 10 times per second
