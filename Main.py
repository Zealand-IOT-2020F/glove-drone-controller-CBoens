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


#TakeOff/landing

# After starting the program you make the drone takeoff by pressing and holding the sensehat joystick
# landing is done by then pressing and holding the sensehat joystick


#Controls

#If you pitch the sensehat forward (45-90degrees) the drone will asecend 20cm
#If you pitch the sensehat backwards (45-90degrees) the drone will descend 20cm
#rolling the sensehat right (45-90degrees) should make the drone Yaw(rotate on own axis) clockwise
#rolling the sensehat left (45-90degrees) should make the drone Yaw(rotate on own axis) counterclockwise
#**This can be dependent on your sensehat!**

#a quick press of the joystick should halt the drone.
