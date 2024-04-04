import time

from Rosmaster_Lib import Rosmaster


car = Rosmaster(debug=True)

delay = 0.0001
for i in range(0, 100):
    car.set_beep(1)
    time.sleep(delay)
    car.set_beep(0)
    time.sleep(delay)
