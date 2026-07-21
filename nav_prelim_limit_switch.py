import time
import board
import pwmio
import math
import adafruit_hcsr04
from analogio import AnalogIn  # get access to analog pins
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

# FOR MOTORS -----------------------------------------------------------------
IN1 = pwmio.PWMOut(board.GP15)
IN1.duty_cycle = 65535
IN2 = pwmio.PWMOut(board.GP14)
IN2.duty_cycle = 65535
IN3 = pwmio.PWMOut(board.GP12)
IN3.duty_cycle = 65535
IN4 = pwmio.PWMOut(board.GP13)
IN4.duty_cycle = 65535

# FOR SERVOS -----------------------------------------------------------------
servoOnePwm = pwmio.PWMOut(board.GP1, duty_cycle=0, frequency=50)
servoOne = servo.Servo(servoOnePwm)
servoTwoPwm = pwmio.PWMOut(board.GP0, duty_cycle=0, frequency=50)
servoTwo = servo.Servo(servoTwoPwm)

# FOR SONIC DISTANCE ----------------------------------------------------------
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP16, echo_pin=board.GP17)  # trigger GP16, echo GP17

# FOR LIGHT SENSOR --------------------------------------------------------------
lightSensorPin = AnalogIn(board.A0)

# FOR LIMIT SWITCH ----------------------------------------------------------
limitSwitch = DigitalInOut(board.GP2)  # choose any unused GPIO
limitSwitch.direction = Direction.INPUT
limitSwitch.pull = Pull.UP


def readLightLevel():
    rawValue = lightSensorPin.value
    volts = 3.3 * rawValue / 65535
    percentValue = rawValue / 65535 * 100
    return round(percentValue, 2)


def readDistance():
    try:
        return round(sonar.distance, 2)
    except RuntimeError:
        return -1


def activateMotor(clockwise, motorNum, speed=0.5):
    firstIn = IN1 if motorNum == 0 else IN3
    secondIn = IN2 if motorNum == 0 else IN4
    if clockwise:
        firstIn.duty_cycle = 65535 - math.floor(speed * 65535)
        secondIn.duty_cycle = 65535
    else:
        firstIn.duty_cycle = 65535
        secondIn.duty_cycle = 65535 - math.floor(speed * 65535)


def stopMotor(motorNum):
    firstIn = IN1 if motorNum == 0 else IN3
    secondIn = IN2 if motorNum == 0 else IN4
    firstIn.duty_cycle = 65535
    secondIn.duty_cycle = 65535


def setServoAngle(angle, servoNum=0):
    servoToMove = servoOne if servoNum == 0 else servoTwo
    servoToMove.angle = angle


def limitSwitchPressed():
    # checks if at this moment the limit switch is pressed
    return limitSwitch.value


def turnRobot(turningRight=True):
    speedToTurn = 0.8  # from 0 to 1
    for i in range(0, 30000):  # can tweak based on wheel length
        activateMotor(turningRight, 0, speedToTurn)
        activateMotor(turningRight, 1, speedToTurn)
    stopMotor(1)
    stopMotor(0)


def stopAllMotors():
    stopMotor(0)
    stopMotor(1)


def goForward(speed=0.8):
    activateMotor(False, 0, speed)
    activateMotor(True, 1, speed)


def goBackwards(speed=0.8):
    activateMotor(True, 0, speed)
    activateMotor(False, 1, speed)


def openClaws():
    setServoAngle(0, 0)
    setServoAngle(0, 1)


def closeClaws():
    setServoAngle(180, 0)
    setServoAngle(180, 1)


def main():
    # move forward for a few seconds, then turn around
    goForward()
    time.sleep(2)
    stopAllMotors()
    turnRobot(True)
    openClaws()
    goForward()
    while True:
        if limitSwitchPressed():  # if it hits a wall
            stopAllMotors()
            closeClaws()
            goBackwards()  # back up for a few seconds
            time.sleep(2)
            turnRobot(True)  # turn right
            goForward()  # move
            time.sleep(2)
            turnRobot(True)  # turn again
            openClaws()  # reopen claws
            break
        time.sleep(0.05)


main()
