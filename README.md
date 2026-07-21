# Northwestern Session 2 - Mechatronics Competition Robot

Competition robot I designed and built for a block-sorting challenge at Northwestern's Mechatronics program (July 2026). Placed 1st out of 30+ students, judged by Professor Marchuk.

**CAD:** [View the full design on OnShape](https://cad.onshape.com/documents/bd7bf225d3cd60975be912fb/w/9dfe725a6ceab4a6fb9d2f20/e/50ae594808063be0acbd73b2?renderMode=0&uiState=6a5fcf8d376c3db27cd99228)

<p float="left">
  <img src="images/robot_photo_1.jpg" width="45%" />
  <img src="images/robot_photo_2.jpg" width="45%" />
</p>

## Overview

The robot navigates the competition area on its own, uses an ultrasonic distance sensor and a limit switch to detect walls, and grips blocks with a claw mechanism. It sorts them by reading the brightness of the surface underneath it with a reflectance sensor.

## Key Design Decisions

**Claw vs. ram-pushing.** Most competitors went with a ram-style design that just pushes blocks around. I built a claw instead. It grips more of the block's surface, so placement ends up a lot more consistent. Full claw geometry and assembly is in the [CAD model](https://cad.onshape.com/documents/bd7bf225d3cd60975be912fb/w/9dfe725a6ceab4a6fb9d2f20/e/50ae594808063be0acbd73b2?renderMode=0&uiState=6a5fcf8d376c3db27cd99228).

## Design Log

The full day-by-day process is documented in `Damon's Design Log.pdf`, included in this repo. It covers the build from July 6 through July 17, including early planning sketches, breadboard photos at each stage, and the code as it evolved from single-component tests to the final integrated robot. It's the rawest look at the actual process, dead ends included, rather than just the finished result.

**Reflectance-based sorting.** A simple reflectance sensor, just an LED and a phototransistor, reads how bright the surface is directly below the robot. Light blocks and dark blocks come back with clearly different readings, which is enough to sort by.

**Straight-line driving through motor calibration.** With no steering system, the robot naturally drifted to one side. Rather than write correction code for it, I just manually tuned the motor duty cycles until it drove straight on its own.

## Hardware

- Raspberry Pi Pico (main controller)
- 2x DC motors (PWM controlled)
- 2x servos (claw mechanism)
- HC-SR04 ultrasonic distance sensor
- Analog light sensor (ambient reference)
- Analog reflectance sensor (block brightness detection)
- Limit switch (wall/obstacle detection)

## Repo Structure

This repo has the full build progression in it, not just the final robot. It goes from small component tests up to the fully integrated system:

| File | Description |
|---|---|
| `cipher.py` | Caesar cipher encrypt/decrypt (early warm-up) |
| `morse_flasher.py` | Blinks a message in Morse code with an LED |
| `button_led_toggle.py` | Basic input/output test, LED controlled by a button |
| `button_counter.py` | Counts button presses |
| `potentiometer_dimmer.py` | Potentiometer controls LED brightness |
| `light_sensor_reader.py` | Reads and prints ambient light level |
| `distance_light_reader.py` | Reads distance and light sensors together |
| `servo_follows_distance.py` | Servo angle tracks live distance readings |
| `motor_servo_test_rig.py` | First integration test — motors, claw, sensors |
| `nav_prelim_limit_switch.py` | Early navigation: drive, detect wall, turn |
| `block_color_sensor.py` | Distinguishes light vs. dark blocks with the reflectance sensor |
| `competition_robot_final.py` | Final competition code — navigation, claw, wall detection |

## From Practice to Final Product

The final robot wasn't built in one sitting, it came together from a stack of smaller tests, and each one solved a specific problem before it became part of the bigger system.

The **button and potentiometer tests** were where I first worked with digital and analog input on the Pico. That analog-read logic carried straight into `light_sensor_reader.py`, and eventually into `block_color_sensor.py`, reading a raw analog value and turning it into a usable threshold is the same idea whether it's brightness for a dimmer or brightness for sorting a block.

The **distance and servo tests** (`distance_light_reader.py`, `servo_follows_distance.py`) is where I worked out how to read a sensor and act on it in real time, before that logic ever touched a motor. By the time I got to `motor_servo_test_rig.py`, I already knew the sensor readings were reliable, so I could focus on getting the motors and claw working without also debugging the sensors at the same time.

`nav_prelim_limit_switch.py` is where the actual navigation logic started coming together: drive forward, detect a wall, react to it. It was rough and the timing was off in a few places, but it proved the core loop worked before I added the claw and sorting logic on top of it.

By the time I got to `competition_robot_final.py`, most of the hard problems had already been solved in isolation. I wasn't debugging sensors, motors, and navigation all at once, I was combining pieces I already trusted, laid out fully in the [CAD assembly](https://cad.onshape.com/documents/bd7bf225d3cd60975be912fb/w/9dfe725a6ceab4a6fb9d2f20/e/50ae594808063be0acbd73b2?renderMode=0&uiState=6a5fcf8d376c3db27cd99228). The biggest remaining challenge was coordination: making sure none of those working pieces interfered with each other once they were all running together. Building it this way, one small working piece at a time, is a big part of why the final robot held up under competition conditions instead of falling apart the first time something unexpected happened.

## Biggest Challenge

The most significant hurdle was managing the complexity and coordination of multiple hardware components. Ensuring that the motors, servos, various sensors, and navigation algorithms worked together seamlessly without introducing conflicts or timing errors required extensive debugging to isolate the root cause of many issues.
