# Northwestern Session 2 - Mechatronics Competition Robot

Competition robot built for a block-sorting challenge at Northwestern's Mechatronics program (July 2026). Placed 1st out of 30+ students, judged by Professor Marchuk.

What it does

The robot drives forward, detects walls/obstacles using an ultrasonic distance sensor and limit switch, and uses a claw mechanism to grab and sort blocks by placing them based on brightness detected under a reflectance sensor.

Key design decisions

- Claw over ram-pushing. Most competitors pushed blocks with a ram-style mechanism. I built a claw instead, more contact area on the block and more reliable, repeatable placement.
- Reflectance-based block detection. A two-element reflectance sensor (LED + phototransistor) reads brightness off the surface directly underneath the robot. Light blocks and dark blocks return distinct brightness values, which the robot uses to decide where to place them.
- Straight-line driving via motor calibration. Manually tuned motor duty cycles to correct for a natural pull, so the robot drives straight without constant correction logic.

Hardware

- Raspberry Pi Pico (main controller)
- 2x DC motors, driven via PWM

- 2x servos (claw)

- HC-SR04 ultrasonic distance sensor

- Analog light sensor (ambient)

- Analog reflectance sensor (block brightness detection)

- Limit switch (wall/obstacle detection)

Repo structure

This repo includes the full build progression, not just the final robot, showing how the code developed from individual component tests up to the final integrated system:

| File | What it does |

|---|---|

| cipher.py | Caesar cipher encrypt/decrypt - early language warm-up |
| morse_flasher.py | Blinks a message via LED in morse code |
| buttonledtoggle.py | Basic digital input/output test |
| button_counter.py | Increments a counter on each button press |
| potentiometer_dimmer.py | Analog input controlling LED brightness |
| lightsensorreader.py | Reads and prints ambient light level |
| distancelightreader.py | Combined distance + light sensor readout |
| servofollowsdistance.py | Servo angle mapped to live distance readings |
| motorservotest_rig.py | First full motor + claw + sensor integration test |
| navprelimlimit_switch.py | Early navigation logic: drive, detect wall, turn |
| blockcolorsensor.py | Reflectance sensor logic for detecting light vs. Dark blocks |
| competitionrobotfinal.py | Final competition code - full navigation, claw control, and wall detection |

Biggest challenge

Keeping track of and coordinating all the components as build complexity grew, motors, two servos, three sensor types, and the navigation logic all had to run together without conflicting or timing out on each other.
