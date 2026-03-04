# Embedded Orientation & Flight Sensor Telemetry System

## Overview
This project demonstrates end-to-end embedded software development,
from microcontroller firmware to Linux-based host applications.

An Arduino microcontroller communicates with a Linux VM over USB serial.
The system supports command-based control and will be extended to include
IMU-based orientation sensing and data visualization.

## Current Features
- Arduino firmware implementing command/response serial protocol
- Linux Python application controlling hardware over /dev/ttyACM*
- VirtualBox-based Linux development environment
- Verified integration and testing using minicom and Python
- IMU (accelerometer + gyroscope) integration
- Real-time orientation data streaming
- Python-based visualization and logging

## Planned Features
- Improved GUI showcasing gyroscopic data
- Basic test artifacts and documentation

## Technologies Used
- C++ (Arduino)
- Python 3
- Linux (Ubuntu)
- USB Serial (CDC ACM)
- Git / GitHub

## How to Run
1. Upload Arduino firmware from `arduino/`
2. Connect Arduino via USB
3. Run:
   ```bash
   python3 linux/serial_control.py


