#!/usr/bin/env python3
# coding: utf-8

import time
from Rosmaster_Lib import Rosmaster

def test_led_effects(rosbot):
    effects = [
        (0, "Stop"),         # Stop any ongoing effect
        (1, "Running Light"),# Running light effect
        (2, "Marquee"),      # Marquee effect
        (3, "Breathing"),    # Breathing light effect
        (4, "Color Wipe"),   # Color wipe effect
        (5, "Color Chase"),  # Color chase effect
        (6, "Flash"),        # Flash effect
    ]

    for effect, description in effects:
        print(f"Activating {description} effect.")
        rosbot.set_colorful_effect(effect, speed=5)  # Adjust speed as necessary
        time.sleep(3)  # Wait for 3 seconds to observe the effect

    # Stop the effect
    print("Stopping any light effects.")
    rosbot.set_colorful_effect(0)

def main():
    try:
        # Initialize Rosmaster with appropriate car type and debug mode enabled
        rosbot = Rosmaster(car_type=1, debug=True)
        # Test LED effects
        test_led_effects(rosbot)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Cleanup, if necessary
        print("Cleanup and exit.")

if __name__ == "__main__":
    main()
