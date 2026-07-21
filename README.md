# Northwestern Session 2 - Mechatronics Competition Robot

Competition robot designed and built for a block-sorting challenge as part of Northwestern University's Mechatronics program (July 2026). Placed 1st out of over 30 students in the challenge, judged by Professor Marchuk.

## Overview

The robot autonomously navigates the competition area, uses an ultrasonic distance sensor and limit switch for wall/obstacle detection, and employs a claw mechanism to grip and pick up blocks. Blocks are sorted based on the surface brightness underneath them, as measured by a reflectance sensor.

## Key Design Decisions

**Claw vs. Ram-pushing:** Most competitors opted for a ram-based design to push blocks. I chose a claw, which provides more surface area contact with the block and generally results in more consistent and reliable placement of sorted items.

**Reflectance-based block sorting:** A simple two-element reflectance sensor (composed of an LED and phototransistor) was used to measure the brightness of the surface directly below the robot. Differentiating between light and dark blocks is achieved by analyzing these reflectance values.

**Straight-line driving via motor calibration:** Without direct steering control, the robot had an inherent tendency to drift to one side. To mitigate this, I bypassed complex correction algorithms and instead manually tuned the duty cycles of the drive motors to ensure the robot travels in a straight line.

## Hardware

- Raspberry Pi Pico (main controller)
- 2x DC motors (controlled via PWM)
- 2x Servos (for the claw mechanism)
- HC-SR04 Ultrasonic Distance Sensor
- Analog Light Sensor (for ambient light reference)
- Analog Reflectance Sensor (for block brightness detection)
- Limit Switch (for wall/obstacle detection)

## Repo Structure

This repository contains code documenting the entire development process, from individual component tests to the fully integrated final robot:

| File | Description |
|---|---|
| `cipher.py` | Caesar cipher encryption and decryption (language warm-up) |
| `morse_flasher.py` | Blinks a message in Morse code using an LED |
| `button_led_toggle.py` | Basic digital input/output test for controlling an LED with a button |
| `button_counter.py` | Increments a counter on each button press |
| `potentiometer_dimmer.py` | Uses a potentiometer to control LED brightness |
| `light_sensor_reader.py` | Reads and prints ambient light levels |
| `distance_light_reader.py` | Reads and prints data from both distance and light sensors |
| `servo_follows_distance.py` | Maps servo angle to real-time distance sensor readings |
| `motor_servo_test_rig.py` | First test rig integrating motors, claw, and sensors |
| `nav_prelim_limit_switch.py` | Initial navigation logic: drive, detect wall, turn |
| `block_color_sensor.py` | Logic for distinguishing light and dark blocks using the reflectance sensor |
| `competition_robot_final.py` | Final code for the competition robot: navigation, claw, wall detection |

## Biggest Challenge

The most significant hurdle was managing the complexity and coordination of multiple hardware components. Ensuring that the motors, servos, various sensors, and navigation algorithms worked together seamlessly without introducing conflicts or timing errors required extensive debugging to isolate the root cause of many issues.
