import Drone
import Controller
import sys
import time

#here you should interact with the drone
print("booting")

drone1 = Drone.Drone('192.1.1.1',8889)
controller1 = Controller.Controller(drone1)

#Diagnostics

#drone1.printinfo()

#drone1.connect()

#drone1.battery()

#Action