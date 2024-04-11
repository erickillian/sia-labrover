#!/usr/bin/env python3
# coding: utf-8

import time

from Rosmaster_Lib import Rosmaster

def test_led_lightbar(rosbot):
    colors = [
        (255, 0, 0),  # Red
        (0, 255, 0),  # Green
        (0, 0, 255),  # Blue
        (255, 255, 0), # Yellow
        (0, 255, 255), # Cyan
        (255, 0, 255), # Magenta
        (255, 255, 255) # White
    ]

    led_id = 0xFF  # Assuming 0xFF addresses all LEDs

    for color in colors:
        red, green, blue = color
        print(f"Setting LED color to RGB({red}, {green}, {blue})")
        rosbot.set_colorful_lamps(led_id, red, green, blue)
        time.sleep(1)  # Wait for 1 second before changing to next color

    # Turn off the LED lightbar after the test
    print("Turning off the LED lightbar.")
    rosbot.set_colorful_lamps(led_id, 0, 0, 0)

try:
    # Initialize Rosmaster with appropriate car type and debug mode enabled
    rosbot = Rosmaster(car_type=1, debug=True)
    # Test LED lightbar
    test_led_lightbar(rosbot)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Cleanup, if necessary
    print("Cleanup and exit.")

