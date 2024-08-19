#!/usr/bin/env python3

import pigpio
import keyboard
import time

# GPIO pin connected to the servo signal line
SERVO_PIN = 17

# Create a pigpio instance
pi = pigpio.pi()
if not pi.connected:
    exit()

# Define the servo pulse width range (in microseconds)
MIN_PULSE_WIDTH = 500
MAX_PULSE_WIDTH = 2500

# Define the range of motion
MIN_ANGLE = 0
MAX_ANGLE = 180

def set_servo_angle(angle):
    pulse_width = MIN_PULSE_WIDTH + (angle / MAX_ANGLE) * (MAX_PULSE_WIDTH - MIN_PULSE_WIDTH)
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)

current_angle = (MIN_ANGLE + MAX_ANGLE) // 2  # Start in the middle

try:
    while True:
        if keyboard.is_pressed('up'):
            current_angle = min(current_angle + 1, MAX_ANGLE)
            set_servo_angle(current_angle)
            time.sleep(0.01)  # Small delay to debounce the key press
        elif keyboard.is_pressed('down'):
            current_angle = max(current_angle - 1, MIN_ANGLE)
            set_servo_angle(current_angle)
            time.sleep(0.01)  # Small delay to debounce the key press
        time.sleep(0.01)  # Small delay to avoid CPU overload
except KeyboardInterrupt:
    pi.set_servo_pulsewidth(SERVO_PIN, 0)
    pi.stop()
