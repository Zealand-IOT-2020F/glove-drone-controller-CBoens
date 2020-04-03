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
    pause()
#Diagnostics

#drone1.printinfo()

#drone1.connect()

#drone1.battery()

#Action