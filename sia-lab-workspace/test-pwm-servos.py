import time
from Rosmaster_Lib import Rosmaster

# Assuming Rosmaster is the class provided, and its methods are to be used
# We'll mock initialization and calls since direct function usage outside the class context is not standard

# Mock function to simulate Rosmaster initialization
def initialize_rosmaster(car_type=1, com="/dev/myserial", delay=0.002, debug=False):
    rosmaster_instance = Rosmaster(car_type, com, delay, debug)
    rosmaster_instance.create_receive_threading()
    time.sleep(0.1)  # Wait for the thread to start and stabilize
    return rosmaster_instance

# Mock function to test individual PWM servo
def test_pwm_servo(rosmaster_instance, servo_id, angle):
    rosmaster_instance.set_pwm_servo(servo_id, angle)
    print(f"Testing PWM servo {servo_id} with angle {angle}")

# Mock function to test all PWM servos
def test_pwm_servo_all(rosmaster_instance, angle_s1, angle_s2, angle_s3, angle_s4):
    rosmaster_instance.set_pwm_servo_all(angle_s1, angle_s2, angle_s3, angle_s4)
    print("Testing all PWM servos with angles:", angle_s1, angle_s2, angle_s3, angle_s4)

# Main procedure to utilize Rosmaster functions for servo testing
def main():
    # Initialize Rosmaster
    rosmaster = initialize_rosmaster(debug=True)

    # Test each PWM servo
    for servo_id in range(1, 5):  # Assuming 4 PWM servos
        test_pwm_servo(rosmaster, servo_id, 90)  # Middle position
        time.sleep(2)  # Delay to observe servo movement
        test_pwm_servo(rosmaster, servo_id, 180)  # Max position
        time.sleep(2)
        test_pwm_servo(rosmaster, servo_id, 0)  # Min position
        time.sleep(2)

    # Test all PWM servos simultaneously
    test_pwm_servo_all(rosmaster, 90, 90, 90, 90)
    time.sleep(2)
    test_pwm_servo_all(rosmaster, 180, 180, 180, 180)
    time.sleep(2)
    test_pwm_servo_all(rosmaster, 0, 0, 0, 0)
    time.sleep(2)

    print("PWM servo testing completed.")

main()
