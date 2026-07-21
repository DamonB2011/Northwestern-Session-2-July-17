import board
import time
from analogio import AnalogIn  # get access to analog pins

# reflectance sensor ("two eyes" - LED + phototransistor) reading the surface below it
blockSensorPin = AnalogIn(board.A1)  # separate analog pin from the ambient light sensor on A0

# threshold tuned by testing against the actual light and dark blocks
# raise this if light blocks are being read as dark, lower it if dark blocks are being read as light
BRIGHTNESS_THRESHOLD = 50.0  # percent


def readBlockBrightness():
    # returns brightness under the sensor as a percent
    rawValue = blockSensorPin.value  # analog converter returns 0 for 0V, 65535 for 3.3V
    percentValue = rawValue / 65535 * 100
    return round(percentValue, 2)


def readBlockColor():
    # returns "light" or "dark" based on brightness threshold
    brightness = readBlockBrightness()
    if brightness >= BRIGHTNESS_THRESHOLD:
        return "light"
    else:
        return "dark"


while True:
    brightness = readBlockBrightness()
    color = readBlockColor()
    print(str(brightness) + "% brightness -> " + color + " block")
    time.sleep(0.1)  # update 10 times per second
