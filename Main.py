import Drone
import Controller
import sys
import time
from signal import pause

#here you should interact with the drone
print("booting")

drone1 = Drone.Drone('127.0.0.1',9000)
controller1 = Controller.Controller(drone1)


while(True):
    time.sleep(0.5)
    if (not controller1.landed):
        controller1.check_roll()
        controller1.check_pitch()

#Diagnostics

#drone1.printinfo()

#drone1.connect()

#drone1.battery()

#Action