import time
from Rosmaster_Lib import Rosmaster

rosmaster = Rosmaster(car_type=1, debug=True)

def test_servo_movement(servo_id, start_angle, end_angle, steps=10, delay=1):
    """Test servo movement by gradually moving from start_angle to end_angle."""
    step_angle = (end_angle - start_angle) / steps
    for step in range(steps + 1):
        angle = start_angle + step * step_angle
        print(f"Moving servo {servo_id} to angle {angle}")
        rosmaster.set_uart_servo_angle(servo_id, angle)
        time.sleep(delay)
    
    # Return servo to starting position
    rosmaster.set_uart_servo_angle(servo_id, start_angle)
    print(f"Returned servo {servo_id} to starting angle {start_angle}")

def check_servo_response(servo_id):
    """Check if the servo is responding to commands."""
    response = rosmaster.get_uart_servo_angle(servo_id)
    if response >= 0:
        print(f"Servo {servo_id} is responding. Current angle: {response}")
    else:
        print(f"Servo {servo_id} is not responding or cannot be read.")

def run_diagnostics():
    """Run diagnostics on servos."""
    for servo_id in range(1, 7):  # Assuming IDs 1-6 for the servos
        print(f"\nTesting Servo ID: {servo_id}")
        check_servo_response(servo_id)
        test_servo_movement(servo_id, 90, 180)  # Example angles
        time.sleep(2)  # Wait 2 seconds before next test


rosmaster.create_receive_threading()  # Start receiving data if necessary
run_diagnostics()  # Run diagnostics to debug servo issues
