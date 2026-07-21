import time
import board
import adafruit_hcsr04
from analogio import AnalogIn  # get access to analog pins

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP16, echo_pin=board.GP17)  # trigger GP16, echo GP17

lightSensorPin = AnalogIn(board.A0)  # on the Pico there are only 3 pins that can do this!


def readLightLevel():
    # returns light level as a percent
    rawValue = lightSensorPin.value  # analog converter returns 0 for 0V, 65535 for 3.3V
    volts = 3.3 * rawValue / 65535
    percentValue = rawValue / 65535 * 100
    return round(percentValue, 2)  # round to 2 decimal places


def readDistance():
    # returns distance in cm
    try:
        return round(sonar.distance, 2)  # in cm, rounded to 2 decimal places
    except RuntimeError:
        return "error"


while True:
    print("Distance (cm): " + str(readDistance()) + ", Light level: " + str(readLightLevel()) + "%")
    time.sleep(0.1)
