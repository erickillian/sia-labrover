import time

from Rosmaster_Lib import Rosmaster


car = Rosmaster(debug=True)

car.set_beep(1)
time.sleep(0.1)
car.set_beep(0)
