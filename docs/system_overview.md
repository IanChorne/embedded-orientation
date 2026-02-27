# System Overview

## Architecture
Arduino firmware communicates with a Linux host over USB serial.
The host application sends commands and receives sensor data.

## Data Flow
Linux Python App → USB Serial → Arduino → Sensors
Arduino → USB Serial → Linux Python App → Visualization

## Rationale
This mirrors embedded systems used in simulation, avionics,
and hardware-in-the-loop environments.
