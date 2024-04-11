import time

from Rosmaster_Lib import Rosmaster


car = Rosmaster(debug=True)

# params are x, y, z.  Not sure why z is needed but x and y control steering and speed
car.set_car_motion(1, 1, 0)
time.sleep(1)
car.set_car_motion(0, 0, 0)


